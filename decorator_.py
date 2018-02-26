# 一般装饰器
import time
import logging
from functools import wraps

def timethis(func):
    """ 
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


# 编写一个带有参数的装饰器

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        @wraps(func)
        def wrapper(*args, **kwargs)
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y