# coding=utf-8

"""
In [1]: b = 5

In [2]: def f2(a):
   ...:     print(a)
   ...:     print(b)
   ...:     b = 9
   ...:

In [3]: f2(3)
3
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-3-ddde86392cb4> in <module>()
----> 1 f2(3)

<ipython-input-2-2304a03d7bfd> in f2(a)
      1 def f2(a):
      2     print(a)
----> 3     print(b)
      4     b = 9
      5

UnboundLocalError: local variable 'b' referenced before assignment

Python 编译函数的定义体时，它判断 b 是局部变量，因为在函数中给它赋值
了。生成的字节码证实了这种判断，Python 会尝试从本地环境获取 b。后面调用 f2(3)
时， f2 的定义体会获取并打印局部变量 a 的值，但是尝试获取局部变量 b 的值时，发现
b 没有绑定值。
"""

"""
关于闭包：
闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义
的非全局变量。函数是不是匿名的没有关系，关键是它能访问定义体之外定义的非全局变
量。
"""


def make_averager():
    series = []   # 自由变量

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

"""
闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，
虽然定义作用域不可用了，但是仍能使用那些绑定。 即内部的函数可以使用外部函数的变量
"""
"""
用法： 
avg = make_avrager() 返回 averager 
然后调用 avg将数值传入
"""

"""
闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，
虽然定义作用域不可用了，但是仍能使用那些绑定
"""


"""
def make_avg():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count
    return averager

这样会报错，报错是因为 count， total是不可变类， 当通过+= 时会创建局部变量，这样count， total就不是
自由变量了，不会保存在闭包中。
为了解决这个问题，Python 3 引入了 nonlocal 声明。它的作用是把变量标记为自由变
量，即使在函数中为变量赋予新值了，也会变成自由变量。如果为 nonlocal 声明的变量
赋予新值，闭包中保存的绑定会更新。最新版 make_averager 的正确实现如示例 7-14 所
示。
"""

def make_avg():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager


# 一个真正的装饰器

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked  # 把被装饰的函数替换成新函数，二者接受相同的参数，而且（通常）
    # 返回被装饰的函数本该返回的值，同时还会做些额外操作。




import pdb;pdb.set_trace()