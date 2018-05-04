# coding=utf-8

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    """
    __getitem__ 方法实现了切片迭代和下标操作
    collections.namedtuple 实现了具名元祖
    in 方法会先找 __contains__ 若找不到则会迭代去搜索
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in
                       self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

deck = FrenchDeck()

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # 获取对应元素的下标
    print(rank_value)
    print(card)
    print(suit_values[card.suit])
    print(rank_value * len(suit_values))
    print("-----------------------------")
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

###################实现二位数组############################

from math import hypot


class Vector(object):
    """
    __str__ 和 __repr__ 这两个特殊方法中的一个，__repr__ 是更好的选择，因为如果一个对象
    没有 __str__ 函数，而 Python 又需要调用它的时候，解释器会用 __repr__ 作为替代
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):  # 自定义bool类型
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)





