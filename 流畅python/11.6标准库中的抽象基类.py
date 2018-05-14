# coding=utf-8

"""
标准库中有两个名为 abc 的模块，这里说的是 collections.abc。为了减少
加载时间，Python 3.4 在 collections 包之外实现这个模块（在
Lib/_collections_abc.py
中，https://hg.python.org/cpython/file/3.4/Lib/_collections_abc.py），因此要与
collections 分开导入。另一个 abc 模块就是 abc（即
Lib/abc.py，https://hg.python.org/cpython/file/3.4/Lib/abc.py），这里定义的是 a
"""

