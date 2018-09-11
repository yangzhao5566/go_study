"""
test for vs pipeline
"""
import redis
import time
from functools import wraps


def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        back = func(*args, **kwargs)
        print("@%.3fs taken for {%s}" % (time.time() - t0, func.__name__))
        return back
    return wrapper


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


@count
def insert():
    for i in range(10000):
        key = "hashkey" + str(i)
        r.hset(key, key, i)


@count
def pipe_insert():
    pipe = r.pipeline()
    for i in range(10000, 20000):
        key = "hashkey" + str(i)
        pipe.hset(key, key, i)
    pipe.execute()


if __name__ == "__main__":
    """
    输出结果：因为少了网络传输过程时间大大减少
    (py36) ➜  redis git:(master) ✗ python  pipe.py
    @1.288s taken for {insert}
    @0.308s taken for {pipe_insert}
    """
    insert()
    pipe_insert()
