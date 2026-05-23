from functools import wraps


def coroutine(func):
    """ Заводит генератор за нас"""
    @wraps(func)
    def inner(*args, **kwargs):
        fn = func(*args, **kwargs)
        next(fn)
        return fn
    return inner
