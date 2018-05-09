# coding=utf-8

"""本章要义
    Python 如何计算装饰器句法
    Python 如何判断变量是不是局部的
    闭包存在的原因和工作原理
    nonlocal 能解决什么问题
"""

""" 装饰器的实质：
@decorate
def target():
    print('running target()')
    
本质：
def target():
    print('running target()')
target = decorate(target)
"""


