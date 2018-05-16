# coding=utf-8

from test2 import test2
from test1 import Test

# def test2():
#     print(Test.__test__)
a = Test.__test__
print(a)

print(a.split('\n'))
print(id(Test))

test2()