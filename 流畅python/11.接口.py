# coding=utf-8

"""
鉴于序列协议的重要性，如果没有 __iter__ 和 __contains__ 方法，Python 会调
用 __getitem__ 方法，设法让迭代和 in 运算符可用。
"""

"""
扑克牌"""

import collections
from random import shuffle  # 为了就地的打乱顺序

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FranchDeck(object):

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    """
    如果只实现了getitem 而不实现__setitem__ 则只实现了不可变的序列协议，可变的序列协还必须
    提供__setitem__方法 
    """
    def __getitem__(self, item):
        return self._cards[item]

    # def __setitem__(self, key, value):
    #     self._cards[key] = value
    #


def set_card(deck, position, card):
    deck._cards[position] = card


FranchDeck.__setitem__ = set_card

