# coding=utf-8

import weakref

"""
有时候需要引用对象，而不让对象存在时间超过所需时间，这经常用在缓存中
引用对象不会增加对象的引用数量， 引用的目标对象称为所指对象，所以弱引用不会妨碍所指对象当
做垃圾回收
"""

a_set = {0, 1}

wref = weakref.ref(a_set)

print(wref())

print(wref)


class Cheese(object):
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()

catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese


print(sorted(stock.keys()))

del catalog

print(sorted(stock.keys()))

del cheese

print(sorted(stock.keys()))

"""
weakref.WeakValueDictionary对应的是WeakKeyDictionary，后者的键是弱引用，
（WeakKeyDictionary 实例）可以为应用中其他部分拥有的对象附加数据，这样就
无需为对象添加属性。这对覆盖属性访问权限的对象尤其有用。
"""

"""
int 和 tuple 实例不能作为弱引用的目标，甚至它们的子类也不行
"""

"""
基本的 list 和 dict
实例不能作为所指对象，但是它们的子类可以轻松地解决这个问题
"""

"""
In [12]: t = (1, 2, 3, 4)

In [13]: b = t[:]

In [14]: id(t)
Out[14]: 4364333688

In [15]: id(b)
Out[15]: 4364333688

In [16]: c = tuple(t)

In [17]: id(c)
Out[17]: 4364333688

元祖使用下标方式来切片的时候不会创建副本，而是返回同一个对象的引用
tuple(t) 获的的也是同一个元祖的引用
"""


"""
set是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。


frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，
也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。
"""
fza = frozenset('a')
adict = {fza: 1, 'b': 2}   #正确
setb = set('a')
bdict = {setb: 1, 'b': 2}   #错误

# 不管是set还是frozenset，Python都不支持创建一个整数的集合。

seta = set(1)   # 错误

setb = set('1')   #  里边放的是可迭代对象

"""
元组、str、bytes 和 frozenset 实例也有这种行为。注意，frozenset 实例不是序列，因此
不能使用 fs[:]（fs 是一个 frozenset 实例）。但是，fs.copy() 具有相同的效果：它
会欺骗你，返回同一个对象的引用，而不是创建一个副本
"""

"""
最小整数池，字符串的复制等都是使用的同一变量，
而元组的使用中使用切片的方式不会产生副本，还是原来地址的引用
"""

"""
简单的赋值不创建副本。
对 += 或 *= 所做的增量赋值来说，如果左边的变量绑定的是不可变对象，会创建新
对象；如果是可变对象，会就地修改。
为现有的变量赋予新值，不会修改之前绑定的变量。这叫重新绑定：现在变量绑定了
其他对象。如果变量是之前那个对象的最后一个引用，对象会被当作垃圾回收。
函数的参数以别名的形式传递，这意味着，函数可能会修改通过参数传入的可变对
象。这一行为无法避免，除非在本地创建副本，或者使用不可变对象（例如，传入元
组，而不传入列表）。
使用可变类型作为函数参数的默认值有危险，因为如果就地修改了参数，默认值也就
变了，这会影响以后使用默认值的调用。
"""