# coding=utf-8

"""
得益于 Python 数据模型，自定义类型的行为可以像内置类型那样自然。实现如此自然的
行为，靠的不是继承，而是鸭子类型（duck typing）
"""

"""
在python3 中__repr__ __str__ __format__ 都必须返回Unicode字符串（str类型），
只有__bytes__方法应该返回字节序列（bytes类型)
"""

from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 私有属性双下划线
        self.__y = float(y)
        print(c for c in self)

    @property
    def x(self):            # 设置self.__x  为只读属性
        return self.__x

    @property
    def y(self):   # 设置self.__y 为只读属性
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        # return tuple(self) == tuple(other)
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[: -1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):     # 从二进制加载
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)

"""
要想创建可散列的类型，不一定要实现特性，也不一定要保护实例属性。只需
正确地实现 __hash__ 和 __eq__ 方法即可。但是，实例的散列值绝不应该变化，因
此我们借机提到了只读特性。
"""


"""
staticmethod  和 classmethod
"""


class Demo(object):
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


"""
>>> Demo.klassmeth() # ➌
(<class '__main__.Demo'>,)
>>> Demo.klassmeth('spam')
(<class '__main__.Demo'>, 'spam')
>>> Demo.statmeth() # ➍
()
>>> Demo.statmeth('spam')
('spam',)

不管怎么调用Demo.klassmeth 它的第一个参数始终是Demo类
"""


brl = 1 / 2.43

print(format(brl, '0.4f'))

print('1 Brl = {rate: 0.2f} USD'.format(rate=brl))

print(format(42, 'b'))

print(format(2/3, '.1%'))


"""
格式化代码时先调用__format__方法， 如果找不到，则会从object继承的方法返回str(my_object)
"""

"""
以双下划线开头的属性，为私有属性
如果以 __mood 的形式（两个前导下划线，尾部没有或最多有一个下
划线）命名实例属性，Python 会把属性名存入实例的 __dict__ 属性中，而且会在前面加
上一个下划线和类名。因此，对 Dog 类来说，__mood 会变成 _Dog__mood；对 Beagle
类来说，会变成 _Beagle__mood。这个语言特性叫名称改写（name mangling）
"""

"""
Python 解释器不会对使用单个下划线的属性名做特殊处理，不过这是很多 Python 程序员
严格遵守的约定，他们不会在类外部访问这种属性。 遵守使用一个下划线标记对象的私
有属性很容易，就像遵守使用全大写字母编写常量那样容易。
"""

"""
一个类实现迭代方法可以实现__iter__ 或者不实现此方法的时候实现__getitem__方法也可以
"""


class Test(object):
    short_name = 'xyzt'
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return 2

    def __eq__(self, other):
        if len(self) != len(other):
            return False

    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass
    



"""
__getitem__ 方法实现之后可以进行切片操作，传入两个参数（self, index) 
index 传入的可能是一个数字，一个是slice方法 然后通过判断来是返回的内容
"""

"""
对 my_obj.x 表达式，Python会检查my_obj 实力有没有名为x的属性， 如果没有，到类（my_obj.__class__) 中查找，
如果还没有，就顺着继承树继续查找，如果依旧找不到，会调用my_obj所属类中定义的__getattr__ 方法，传入
self和属性名称的字符串形式（如 'x')
"""

import pdb;pdb.set_trace()