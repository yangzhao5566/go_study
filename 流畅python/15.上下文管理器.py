# coding=utf-8

"""
不管是for还是while 当执行完循环之后后边才会执行else
还有try之后如果不报错则执行else
"""

"""
上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。with 语句开始运行时，会在
上下文管理器对象上调用 __enter__ 方法。
with 语句运行结束后，会在上下文管理器对
象上调用 __exit__ 方法，以此扮演 finally 子句的角色。
"""


class LookingGlass:
    def __enter__(self): # 1
        import sys
        self.original_write = sys.stdout.write  # 2
        sys.stdout.write = self.reverse_write  # 3
        return 'JABBERWOCKY'  # 4

    def reverse_write(self, text):  # 5 可以在上下文中做一些事情，比如反转字符串
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):  # 6
        import sys   # 7
        sys.stdout.write = self.original_write  # 8
        if exc_type is ZeroDivisionError:  # 9
            print('Please DO NOT divide by zero!')
            return True   # 10

"""
❶ 除了 self 之外，Python 调用 __enter__ 方法时不传入其他参数。
❷ 把原来的 sys.stdout.write 方法保存在一个实例属性中，供后面使用。
❸ 为 sys.stdout.write 打猴子补丁，替换成自己编写的方法。
❹ 返回 'JABBERWOCKY' 字符串，这样才有内容存入目标变量 what。
❺ 这是用于取代 sys.stdout.write 的方法，把 text 参数的内容反转，然后调用原来
的实现。
❻ 如果一切正常，Python 调用 __exit__ 方法时传入的参数是 None, None, None；如
果抛出了异常，这三个参数是异常数据，如下所述。
❼ 重复导入模块不会消耗很多资源，因为 Python 会缓存导入的模块。
❽ 还原成原来的 sys.stdout.write 方法。
❾ 如果有异常，而且是 ZeroDivisionError 类型，打印一个消息……
❿ ……然后返回 True，告诉解释器，异常已经处理了。
⓫ 如果 __exit__ 方法返回 None，或者 True 之外的值，with 块中的任何异常都会向上
冒泡。
"""

"""
关于上下文管理器：
closing： 如果对象提供了close()方法，但是没有实现__enter__/__exit__ 协议，那么可以
使用这个函数构建上下文管理器。
suppress构建临时忽略指定异常的上下文管理器。
@contextmanager
这个装饰器把简单的生成器函数变成上下文管理器，这样就不用创建类去实现管理器
协议了。
ContextDecorator
这是个基类，用于定义基于类的上下文管理器。这种上下文管理器也能用于装饰函
数，在受管理的上下文中运行整个函数。
ExitStack
这个上下文管理器能进入多个上下文管理器。with 块结束时，ExitStack 按照后进
先出的顺序调用栈中各个上下文管理器的 __exit__ 方法。如果事先不知道 with 块要进
入多少个上下文管理器，可以使用这个类。例如，同时打开任意一个文件列表中的所有文
件。
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield "ABCDEFGH"   # 产出一个值，这个值会绑定到with语句中as自居的目标变量上执行
    # with 块中的代码时，这个函数会在这一点暂停。
    sys.stdout.write = original_write













