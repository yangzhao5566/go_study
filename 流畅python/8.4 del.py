# coding=utf-8

"""
del 语句删除名称， 而不是对象，del命令可能会导致对象被当做垃圾回收， 但是仅当做删除的变量
保存的是对象的最后一个引用，或者无法的到对象时。
重新绑定也可能会导致对象的引用变量归零，导致对象被销毁
"""
import weakref
import inspect
import reprlib

"""
weakref.finalize 模块会监视一个对象，当这个对象没有引用的时候会调用后边的回调函数
"""

s1 = {1, 2, 3}

s2 = s1


def bye():  # 这个函数一定不能是要销毁的对象的绑定方法，否则会有一个指向对象的引用。
    print('Gone with the wind...')


class test(object):
    pass

print(test.__name__)

ender = weakref.finalize(s1, bye)  # 在 s1 引用的对象上注册 bye 回调。

print(ender.alive)

del s1

print(ender.alive)

s2 = 'spam'


go = globals()
print(go.values())
glob = {}
for k, v in list(go.items()):
    if inspect.isclass(v):
        glob[k] = v

print(glob)





