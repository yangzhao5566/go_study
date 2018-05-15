# coding=utf-8

"""
标准库中有两个名为 abc 的模块，这里说的是 collections.abc。为了减少
加载时间，Python 3.4 在 collections 包之外实现这个模块（在
Lib/_collections_abc.py
中，https://hg.python.org/cpython/file/3.4/Lib/_collections_abc.py），因此要与
collections 分开导入。另一个 abc 模块就是 abc（即
Lib/abc.py，https://hg.python.org/cpython/file/3.4/Lib/abc.py），这里定义的是 a
"""
import abc
import random

"""
在函数上堆叠装饰器的顺序通常很重要，@abstractmethod 的文档就特别指出：
与其他方法描述符一起使用时，abstractmethod() 应该放在最里层，……
也就是说，在 @abstractmethod 和 def 语句之间不能有其他装饰器。
"""


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
        在抽象类中，抽象方法可以实现代码，即便实现了，子类也必须覆盖抽象方法，但是在
        子类中可以使用super()函数调用抽象方法，为它添加功能，而不是从头开始实现
        """

    def loaded(self):
        """
        如果至少有一个元素，返回True 否则返回False
        :return:
        """
        # raise LookupError

    def inspect(self):  # 抽象类中可以包含具体方法
        """返回一个有序元祖，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


"""
Tombola的具体子类
"""


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


"""
白鹅类型的一个基本特性（也是值得用水禽来命名的原因）：即便不继承，也有办法把一
个类注册为抽象基类的虚拟子类
"""
from random import randrange

@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
