# coding=utf-8

import time
# from test2 import test2


class Test(object):
    __test__ = "test"

    def __init__(self):
        print("aa")


print(Test.__test__)

Test.__test__ = 'bb'
print(id(Test))
print(Test.__test__)


"""
导入模块时是把模块从头到尾执行一遍
"""