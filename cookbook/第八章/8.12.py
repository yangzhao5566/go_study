"""
定义接口或者抽象基类
"""

from abc import ABCMeta, abstractmethod
import io


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

"""
抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现特定接口
"""


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError("Expected an IStream")

    pass


"""除了继承，还可以通过注册方式让牟特类实现抽象基类"""
IStream.register(io.IOBase)

f = open("foo.txt")
isinstance(f, IStream)


"""
@abstractmethod 还能注解静态方法、类方法和 properties 。 你只需保证这个注解紧靠在函数定义前即可：
"""


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self):
        pass


