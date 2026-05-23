# ETL Pipeline

# Data-driven модели (системы)
# input: пользовательские данные
# output: удобное представление
# Extract-, Transform-, Load- генераторы

# Композиция генераторов
# Конвейер - псевдоасинхронность
# Псевдоасинхронность потому, что всё происходит в одном потоке
# Хотя мы действительно выполняем одно действие (например, чтение следующего бача), не дожидаясь выполнения другого


import datetime
import json
import logging
import time
from os import PathLike
from typing import Generator

from src.coroutine import coroutine
from src.fetcher import BaseFetcher, FileFetcher
from src.loader import BaseLoader, FileLoader

logger = logging.getLogger(__name__)


# Generator[1, 2, 3] 1 - хз, 2 - ввод данных юзера в yield (через send), 3 - возврат

def extract_generator(filepath: str | PathLike[str]):
    """
    Фабричный метод
    Сгенерируй мне некоторый декоратор
    Который ...
    """
    @coroutine # Заводит генератор
    # По логике в next_node передаём transform
    def extract(fetcher: BaseFetcher, next_node: Generator) -> Generator[None, datetime.datetime, None]:
        # Цикл: принимает значения (например, дату последней записи) - отдаю управление пользователю
        while last_updated := (yield):
            logger.info(
                "Quering entities with modified date greater than %s, with query %s",
                last_updated,
                filepath,
            )
            # Получаем батч
            for result in fetcher.fetch_batch(url_or_path=filepath, batch_size=20, last_updated=last_updated):
                logger.info(f"Read item {result}")
                next_node.send(result) # Передаём результат бача в другой узел
            # Вот такая вот цепочка обработки
    return extract


def transform_generator():
    @coroutine
    def transform(next_node: Generator) -> Generator[None, list[str], None]:
        while data := (yield):
            logger.info("Transformation step started")
            batch = []
            for serialized_data in data:
                deserialized_data = json.loads(serialized_data)
                batch.append(deserialized_data)
            logger.info("Transformed %s records", len(data))
            next_node.send((batch, datetime.datetime.now(datetime.timezone.utc)))
    return transform


def save_generator(
    filepath: str,
):
    @coroutine
    def save_generator(loader: BaseLoader):
        while data := (yield):
            t = time.perf_counter()
            # Сохраняет в файл
            lines = loader.load_batch(filename=filepath, data=data[0])
            elapsed = time.perf_counter() - t
            logger.info(
                "Saving %s records in %s seconds",
                lines,
                elapsed,
            )
    return save_generator


def build_pipeline(
    fetcher: BaseFetcher,
    loader: BaseLoader,
    file_from_read: str | PathLike[str],
    file_to_save: str | PathLike[str],
):
    loader_gen = save_generator(file_to_save)

    transformer_gen = transform_generator()

    extractor_gen = extract_generator(file_from_read)

    saver = loader_gen(loader=loader)

    transformer = transformer_gen(next_node=saver)

    extractor = extractor_gen(fetcher=fetcher, next_node=transformer)

    return extractor


def start_pipeline(pipeline: Generator):
    pipeline.send(datetime.datetime.now(datetime.timezone.utc))


if __name__ == "__main__":
    fetcher = FileFetcher()
    loader = FileLoader()

    pipeline = build_pipeline(
        fetcher=fetcher,
        loader=loader,
        file_from_read="./data/read.jsonlines",
        file_to_save="./data/write.jsonlines",
    )
    start_pipeline(pipeline=pipeline)
