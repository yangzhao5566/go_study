# coding=utf-8

"""
不能重载内置类型的运算符
不能新建运算符，只能重载现有的
某些运算符不能重载——is、and、or 和 not（不过位运算符 &、| 和 ~ 可以）
"""

"""
- (__neg__) 
+ (__pos__)
~ (__invert__) 
运算符的一个基本规则： 始终返回一个新的对象，也就是说，不能修改self, 要创建病返回合适类型的
新实例
"""
from itertools import count
from itertools import islice
from itertools import cycle
from itertools import izip_longest
"""
count(初值=0， 步长=1)
"""

for i in count(10, 2):
    if i > 20:
        break
    else:
        print(i)


for i in islice(count(10), 5):   # 迭代5次后停止
    print(i)


count = 0
for item in cycle('XYZ'):  # 无限循环可迭代对象 知道break停止
    if count > 7:
        break
    print(item)
    count += 1


for item in izip_longest("ABCD", "xy", fillvalue='BLANK'):
    print(item)

"""
def __add__(self, other):
    try:
        pairs = izip_longest(self, other, fillvalue=0.0)
        return Vector(a+b for a, b in pairs)
    except TypeError:
        return NotImplemented
    
def __radd__(self, other):
    return self + other
    
    
def __mul__(self, scalar):
    if isinstance(scalar, numbers.Real):
        return Vector(n * scalar for n in self)
    
def __rmul__(self, scalar):
    return self * scalar

"""

"""
Python 为中缀运算符特殊方法提供了特殊的分派机制。对
表达式 a + b 来说，解释器会执行以下几步操作（见图 13-1）。
(1) 如果 a 有 __add__ 方法，而且返回值不是 NotImplemented，调用 a.__add__(b)，
然后返回结果。
(2) 如果 a 没有 __add__ 方法，或者调用 __add__ 方法返回 NotImplemented，检查 b
有没有 __radd__ 方法，如果有，而且没有返回 NotImplemented，调用b.__radd__(a)，然后返回结果。
如果 b 没有 __radd__ 方法，或者调用 __radd__ 方法返回 NotImplemented，抛出
TypeError，并在错误消息中指明操作数类型不支持。
"""