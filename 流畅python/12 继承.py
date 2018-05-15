# coding=utf-8

"""
子类化内置类型，内置类型的方法不会被调用子类覆盖的方法
"""


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)

dd['two'] = 22

dd.update(three=2)

print(dd)


"""
直接子类化内置类型（如 dict、list 或 str）容易出错，因为内置类型的
方法通常会忽略用户覆盖的方法。不要子类化内置类型，用户自己定义的类应该继承
collections 模块
"""
import collections


class Doppe(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


d = Doppe(one=1)

d["two"] = 2

d.update(three=2)


class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):  # B, C 调换顺序则结果也不一样
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)   # 调用指定的pong方法  这样写必须传入一个类的实例直接在类上调用实例方法时，
        # 必须显式传入 self 参数，因为这样访问的是未绑定方法（unbound method）。


"""
若想把方法调用委托给超类，推荐的方式是使用内置的 super() 函数。在 Python 3 中，
这种方式变得更容易了，如示例 12-4 中 D 类的 pingpong 方法所示。 然而，有时可能需
要绕过方法解析顺序，直接调用某个超类的方法——这样做有时更方便。
"""

"""
调用顺序总结，先在本身找，找不到会去类继承的第一个类里找，然后第二个，以此类推，直到object
"""
d = D()
d.pong()

C.pong(d)   # 超类中的方法都可以直接调用，此时要把实例作为显式参数传入。

print(D.__mro__)


import dateutil







