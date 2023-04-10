import logging

from functools import wraps


logger = logging.getLogger('db')


def exception_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            logger.error("ExceptionCheckAnimeVost", exc_info=ex)
    return wrapper
