"""
简化数据结构的初始化
"""

import math


class Structure:
    _fields = []

    def __init__(self, *args):
        print(args)
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure):
    _fields = ["name", "shares", "price"]


class Point(Structure):
    _fields = ["x", "y"]


class Circle(Structure):
    _fields = ["radius"]

    def area(self):
        return math.pi * self.radius ** 2

