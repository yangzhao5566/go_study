"""
在函数上添加包装饰器
"""

import time
from functools import wraps


def timethis(func):
    """
     Decorator that reports the execution time
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


