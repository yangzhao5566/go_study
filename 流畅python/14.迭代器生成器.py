# coding=utf-8

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


"""
可迭代的对象
　　使用 iter 内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的
__iter__ 方法，那么对象就是可迭代的。序列都可以迭代；实现了 __getitem__ 方
法，而且其参数是从零开始的索引，这种对象也可以迭代。
我们要明确可迭代的对象和迭代器之间的关系：Python 从可迭代的对象中获取迭代器。
"""

s = 'ABC'

it = iter(s)

while True:
    try:
        print(next(it))

    except StopIteration:
        del it
        break

"""
标准的迭代器接口有两个方法：
__next__ 返回下一个可用的元素，如果没有元素了，抛出异常StopIteration 异常

__iter__ 返回self 一般在应该使用可迭代对象的地方使用迭代器，例如在for循环中
"""

"""
Python中一个实现了_iter_方法和_next_方法的类对象，就是迭代器
"""
class SentenceIterator(object):  # 迭代器要实现__next__方法和__iter__方法并返回自身
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word   #  必须每次只返回一个对象

    def __iter__(self):
        return self   # 迭代器的__iter__必须返回自身


ss = SentenceIterator('hello world fm yz')

for i in ss:
    print(i)



##################生成器函数################

"""
只要函数中有yield 则这个函数就是生成器
"""
class Sentences(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):   # 生成器函数，调用时会构建一个实现了迭代接口的生辰器对象
        for word in self.words:
            yield word
        return


"""
re.finditer 函数是re.findall 函数的多谢版本，返回的不是列表，而是一个生成器
"""

class Sentencess(object):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


def gen_AB():
    print('START')
    yield 'A'
    print('continue')
    yield "B"
    print('END.')

"""
只有 for 循环迭代 res2 时，gen_AB 函数的定义体才会真正执行。for 循环每次迭代
时会隐式调用 next(res2)，前进到 gen_AB 函数中的下一个 yield 语句。注
意，gen_AB 函数的输出与 for 循环中 print 函数的输出夹杂在一起。
"""
res = (x*3 for x in gen_AB())   # 这里不会执行gen_AB 函数 当下边调用的时候才会使用

for i in res:
    print('---', i)
