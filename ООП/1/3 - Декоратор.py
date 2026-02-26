# Точка зрения ШАД - мы редко будем писать свои декораторы.
"""
Функция может принимать в качестве аргумента фукнцию
Бывает, что функция - единственный аргумент

Декоратор в сути своей - функция, принявшая в качестве ед. аргумента другую фукнцию
"""
from functools import wraps

def log_calls(func):
    @wraps(func) # решает проблему (*)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__}{args, kwargs}")
        result = func(*args, **kwargs)
        print(f"[RET] {func.__name__} -> {result}")
        return result
    return wrapper

@log_calls # Экв f = log_calls(pow_int); f(2, 10)
def pow_int(x: int, y: int) -> int:
    """power int"""
    return x ** y

pow_int(2, 10)
print(pow_int.__name__, pow_int.__doc__) # (*) wrapper None
# Мы не хотим, чтобы название или документация функции менялось...



"""
ПОЛИТИКА retry
"""


def log_calls(func):
    @wraps(func)
    def
    
    
@log_calls
def pow_int(x: int, y: int):
    ...