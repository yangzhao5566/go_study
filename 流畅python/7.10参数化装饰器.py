# coding=utf-8

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)  # 在集合中移除func discard 为移除但是不存在时会报错

        return func
    return decorate


import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):  # 1
    def decorate(func):  # 2
        def clocked(*_args):  #3
            t0 = time.time()
            _result = func(*_args)  #4
            elapsed = time.time() -t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # 5
            result = repr(_result)    # 6
            print(fmt.format(**locals()))  #7
            return _result   # 8
        return clocked  # 9
    return decorate  # 10


"""
❶ clock 是参数化装饰器工厂函数。
❷ decorate 是真正的装饰器。
❸ clocked 包装被装饰的函数。
❹ _result 是被装饰的函数返回的真正结果。
❺ _args 是 clocked 的参数，args 是用于显示的字符串。
❻ result 是 _result 的字符串表示形式，用于显示。
❼ 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量。
❽ clocked 会取代被装饰的函数，因此它应该返回被装饰的函数返回的值。
❾ decorate 返回 clocked。
❿ clock 返回 decorate。
⓫ 在这个模块中测试，不传入参数调用 clock()，因此应用的装饰器使用默认的格式
str。
"""

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)