"""
关于类的私有方法和私有属性
"""

"""
_xx 以单下划线开头的表示的是proected类型的变量。 即保护类型只能允许其本身和子类进行访问
__xx双下划线表示的是私有类型的变量，只能允许这个类本身进行访问，子类也不可以用于命名一个
类属性（类变量），调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）
"""
import math


class Pub(object):
    _name = "protected 类型的变量"
    __info = "私有类型的变量"

    def _func(self):
        print("这是一个protected类型的方法")

    def __func2(self):
        print("这是一个私有类型的方法")

    def get(self):
        return self.__info


##################创建可管理的属性##################
class Person(object):
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

"""
不要写下边这种没有做任何其他额外操作的property
"""


class Persons:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class A(object):
    def spam(self):
        print("A.spam")


class B(A):
    def spam(self):
        print("B.spam")
        super().spam()


class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

############## 对于继承的property 的修改如下################


class SubPerson(Person):
    @Person.first_name.getter
    def first_name(self):
        print('Getting name')
        return super().first_name

"""
在子类中扩展一个property可能会引起很多不易察觉的问题， 因为一个property其实是 getter、
setter 和 deleter 方法的集合，而不是单个方法。 因此，当你扩展一个property的时候，
你需要先确定你是否要重新定义所有的方法还是说只修改其中某一个。
"""








