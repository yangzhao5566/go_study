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


def tag(name, *content, cls=None, **attrs):
    """生成多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s=%s' % (attr, value)
                           for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


tag('br')

tag('p', 'hello')

tag('p', 'hello', 'world')

tag('p', 'hello', id=22)

tag('p', 'hello', 'world', cls='sidebar')

tag(content='testing', name="img")

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}

tag(**my_tag)

"""
Bobo 是怎么知道函数需要哪个参数的呢？它又是怎么知道参数有没有默认值呢？
函数对象有个 __defaults__ 属性，它的值是一个元组，里面保存着定位参数和关键字
参数的默认值。仅限关键字参数的默认值在 __kwdefaults__ 属性中。然而，参数的名
称在 __code__ 属性中，它的值是一个 code 对象引用，自身也有很多属性。
"""


def clip(text, max_len=80):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before > 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)

        return text[: end].rstrip()

"""
clip.__defaults__ 可以看到带默认值参数的默认值
clip.__code__.co_varnames 可以看到函数内部的所有参数
clip.__code__.co_argcount 可以看到函数需要的参数的个数
('text', 'max_len', 'end', 'space_before', 'space_after')


这里不包含前缀为 * 或 ** 的变长
参数。参数的默认值只能通过它们在 __defaults__ 元组中的位置确定，因此要从后向
前扫描才能把参数和默认值对应起来。
"""

from functools import reduce
from operator import mul
from operator import itemgetter
from operator import attrgetter
from collections import namedtuple


def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


def fact1(n):
    return reduce(mul, range(1, n+1))


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(2, 0)

for city in metro_data:
    print(cc_name(city))

LatLong = namedtuple('LatLong', 'lat long')

Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

from operator import methodcaller
"""
它的作用与
attrgetter 和 itemgetter 类似，它会自行创建函数。methodcaller 创建的函数会在
对象上调用参数指定的方法，
"""
s = 'The time has come'

upcase = methodcaller('upper')

print(upcase(s))


hiphenate = methodcaller('replace', " ", "-")  # 第一个参数为方法，后边的为参数

print(hiphenate(s))

####################partical ###################
from functools import partial

# 将加法运算的一个参数固定为3
triple = partial(mul, 3)
triple(7)
list(map(triple, range(1, 10)))

picture = partial(tag, 'img', cls='pic-frame')   # 可以指明要赋值的参数

picture(src='wumpus.jpeg')
print(picture)


