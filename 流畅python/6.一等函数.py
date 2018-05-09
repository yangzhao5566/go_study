# coding=utf-8

from abc import ABC
from abc import abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    """
     这里需要一个说明，通过继承ABC类，并且通过@abstractmethod 的方法必须要在子类中实现
     否则会报错
     参考：https://foofish.net/guide-python-static-class-abstract-methods.html
     或者可以这么写：
     def discount(self):
         raise NotImplementedError

    """
    @abstractmethod
    def discount(self, order):
        """
        返回折扣金额（正值）
        :param order:
        :return:
        """


"""
更好的做法是把各个折扣规则改写成函数
享元是可共享的对象，可以同时在多个上下文中使用。
这样不必在每个新的上下文（这里是 Order 实例）中使用相同的策略时不断新建具体策略对象，
从而减少消耗。因此，为了避免“策略”模式的一个缺点（运行时消耗）
"""


class FdelityPromo(Promotion):
    """为积分1000或以上的顾客提供5%折扣"""
    def discount(self, order):
        return order.total() * .05 if order.cutomer.fielity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1

        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

"""
globals() 
返回一个字典，表示当前的全局符号表。这个符号表始终针对当前模块（对函数或方
法来说，是指定义它们的模块，而不是调用它们的模块）。
"""
print(globals())

import inspect # 此模块中包含了好多判断的方法
"""
promos = [func for name, func in
 inspect.getmembers(promotions, inspect.isfunction)]
 
把所有的折扣方法写到promotions文件中通过导入到当前文件然后 通过inspect 来判断是否是function
把所有的方法加载到当前的文件下
参见 示例 6-8

inspect.getmembers 函数用于获取对象（这里是 promotions 模块）的属性，第二个
参数是可选的判断条件（一个布尔值函数）。我们使用的是 inspect.isfunction，只
获取模块中的函数。
"""

promos = [globals()[name] for name in globals() if name.endswith('_promo')
          and name != 'best_promo']

import pdb;pdb.set_trace()