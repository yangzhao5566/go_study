"""
duck object
"""

import abc


class Duck(abc.ABC):
    """duck object"""
    @abc.abstractmethod
    def display(self):
        """因为每个鸭子的样貌不一样所以这里需要子类来实现"""
    def quack(self):
        print("呱呱")

    def swim(self):
        print("我会游泳")


"""
超类的分解和组和因为有些属性不是每个鸭子都有的所以把一些功能拆分出来形成单独的抽象类，
然后当需要的时候再继承
"""


class Duck(abc.ABC):
    @abc.abstractmethod
    def display(self):
        """因为每个鸭子的样貌不一样所以这里需要子类来实现"""

    def swim(self):
        print("我会游泳")


class Quackable(object):
    def quack(self):
        print("呱呱")


class Flyable(abc.ABC):
    @abc.abstractmethod
    def fly(self):

