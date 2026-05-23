import json
from abc import ABC, abstractmethod
from os import PathLike


class BaseLoader(ABC):
    @abstractmethod
    def load_batch(self, filename: str | PathLike[str], data: list[dict]) -> int:
        ...


class FileLoader(BaseLoader):
    def load_batch(self, filename: str | PathLike[str], data: list[dict]) -> int:
        with open(filename, 'a', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        return len(data)
