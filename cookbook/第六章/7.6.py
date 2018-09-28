"""
定义匿名或内联函数
"""

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']

sorted(names, key=lambda name: name.split()[-1].lower())


x = 10
a = lambda y: x+y
x = 20
b = lambda y: x+y
print(a(10))
print(b(10))

"""
lambda中的变量是自由变量，在运行时绑定值，而不是定义时就绑定
"""