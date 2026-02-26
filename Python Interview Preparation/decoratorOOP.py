from abc import ABC, abstractmethod

class ProcessABC(ABC):
    @abstractmethod
    def calculate(self, *args, **kwargs):
        ...
        
        
class DBProcess(ProcessABC):
    def calculate(self, *args, **kwargs):
        return print(*args, **kwargs)
    
class CachedProcess(ProcessABC):
    def __init__(self, process: ProcessABC, cache: dict[str, str] | None = None):
        self._process = process
        self._cache = cache
        
    def calculate(self, *args, **kwargs):
        new_kwargs = {}
        for key in kwargs:
            if key in self._cache:
                new_kwargs[key] = self._cache[key]
        self._process.calculate(*args, **kwargs)
        
        # Типичный пример реализации паттерна декоратора в ООП
        
        
class Decorator:
    def __init__(self):
        ...
        
    def __call__(self, func):
        ...
        
# потом @Decorator()?
# или my_class = Decorator(...)


# Backend ORM - если быстрый проект, ничего такого. Если контррль есть над ORM-кой
# Если высоконагруженный - такое себе. Не всегда эффективный запрос. Через сырой SQL иногда быстрее
# А сложная операция вставки проще ORM


# Часто для запросов данных используется чистый SQL
# А для модификации ORM
# Command Query Segregation
# Давайте разделим запросы на получение и мод