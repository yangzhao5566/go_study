# coding=utf-8

##################递归调用################


def factorial(n):
    """
    :param n:
    :return: n!
    """
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial

print(list(map(fact, range(10))))

####################高阶函数##################

"""
接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order
function）例如 map函数
"""

# 根据反向来排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def reverse(word):
    return word[::-1]


sorted(fruits, key=reverse)

from functools import reduce
from operator import add

reduce(add, range(100))

"""
all(iterable) 和 any(iterable) 函数
如果 iterable 的每个元素都是真值，返回 True；all([]) 返回 True。
只要 iterable 中有元素是真值，就返回 True；any([]) 返回 False。
"""

any([0, 1])  # 返回True
all([0, 1])  # 返回False

#######################callalbe####################

import random


class BingoCage(object):

    def __init__(self, items):
        self._items = items
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


