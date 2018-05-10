# coding=utf-8

"""
python内置了三个用于装饰方法的函数：
classmethod
property
staticmethod
"""
import functools

"""
functools.lru_cache装饰器用来将结果缓存起来，当程序计算比较复杂的时候可以使用此装饰器
使用方法:
functools.lru_cache()
括号里可以接受参数 functools.lru_cache(maxsize=128, typed=False) 
maxsize 为缓存的个数，为了得到最佳性能，maxsize 应该设为 2 的幂
typed 参数如果设为 True，把不同
参数类型得到的结果分开保存，
由于functools.lru_cache() 是用字典来储存结果的，所以要求被装饰的函数的参数都是可散列的，
即不可变类型
"""


@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# 单个分派函数
import html
from collections import abc
import numbers
from functools import singledispatch

"""
functools.singledispatch 装饰器可以把整体方案拆分成多个模
块，甚至可以为你无法修改的类提供专门的函数

使用 @singledispatch 装饰的普通函
数会变成泛函数（generic function）：根据第一个参数的类型，以不同方式执行相同操作
的一组函数。
"""

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


from functools import singledispatch
import numbers


@singledispatch
def sort_type(obj):
    print(obj, type(obj), 'obj')


@sort_type.register(str)
def _(text):
    print(text, type(text), 'str')


@sort_type.register(numbers.Integral)
def _(n):
    print(n, type(n), 'int')


import pdb;pdb.set_trace()