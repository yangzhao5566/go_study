# coding=utf-8

from test1 import Test

# def test2():
#     print(Test.__test__)
a = Test.__test__

def test2():
    print(a)

    print(a.split('\n'))
    print(id(Test))


