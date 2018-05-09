# coding=utf-8

"""
函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用
时运行。这突出了 Python 程序员所说的导入时和运行时之间的区别
"""

"""
装饰器的一个关键特性是，他们在被装饰的函数定义之后立即运行，这同时是在导入时发生的

以下写的与平常用的装饰器有区别：
装饰器函数与被装饰的函数在同一个模块中定义。实际情况是，装饰器通常在一个模
块中定义，然后应用到其他模块中的函数上。
register 装饰器返回的函数与通过参数传入的相同。实际上，大多数装饰器会在内
部定义一个函数，然后将其返回。
"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
