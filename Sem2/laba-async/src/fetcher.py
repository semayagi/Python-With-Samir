from abc import ABC, abstractmethod
from datetime import datetime
from os import PathLike
from typing import Generator


class BaseFetcher(ABC):

    @abstractmethod
    def fetch_batch(self, url_or_path: str | PathLike[str], batch_size: int, last_updated: datetime) -> Generator[list[str], None, None]:
        ...

# Файл мог быть слишком большим и читать его целиком - дорого. Читаем пачками
class FileFetcher(BaseFetcher):
    # Можем фильтровать по последней дате записи - поэтому передаём. А тут просто так передал
    def fetch_batch(self, url_or_path: str | PathLike[str], batch_size: int, last_updated: datetime) -> Generator[list[str], None, None]:
        batch = []
        with open(url_or_path, 'r') as f:
            for line in f:
                batch.append(line)
                if len(batch) == batch_size:
                    yield batch
