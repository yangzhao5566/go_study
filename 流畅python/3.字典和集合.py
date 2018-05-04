# coding=utf-8

"""
主要内容
常见的字典方法
如何处理查找不到的键
标准库中dict类型的变种
"""

"""
如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不可变的
而且这个对象需要实现__hash__()方法 而且还要有__qe__方法

"""

##############字典推导式#################


DIAL_CODES = [
 (86, 'China'),
 (91, 'India'),
 (1, 'United States'),
 (62, 'Indonesia'),
 (55, 'Brazil'),
 (92, 'Pakistan'),
 (880, 'Bangladesh'),
 (234, 'Nigeria'),
 (7, 'Russia'),
 (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}


country_code.items()
country_code.keys()

"""
若字典里有键k，则把它对应的值设置为 default，然
后返回这个的旧的值；若无，则让 d[k] = default，然后返回
default
"""
country_code.setdefault(99, 'Japan') # 查找99 对应的键查找到则更新为japan 找不到则设置


#####################defaultdict#############################
"""
In [3]: import collections

In [4]: s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

In [5]: d = collections.defaultdict(list)

In [6]: for k, v in s:
   ...:     d[k].append(v)
   ...:

In [7]: d
Out[7]: defaultdict(list, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

In [8]: d['aaa']
Out[8]: []

d['ccc'] 会返回一个[]
但 d.get('ccc') 会什么也不返回
"""

"""
所有的映射类型在处理找不到的键的时候，都会牵扯到 __missing__ 方法。这也是这个
方法称作“missing”的原因。虽然基类 dict 并没有定义这个方法，但是 dict 是知道有这
么个东西存在的。也就是说，如果有一个类继承了 dict，然后这个继承类提供了
__missing__ 方法，那么在 __getitem__ 碰到找不到的键的时候，Python 就会自动调用
它，而不是抛出一个 KeyError 异常。
"""

"""
__missing__ 方法只会被__getitem__调用，如d[k]。
 提供了__missing__ 方法对get 或者 __contains__ 这些方法的使用没有影响
 
"""


class StrKeyDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()


######################OrderDict#########################

from collections import ChainMap
from collections import Counter
from collections import UserDict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "d": 4}
dict3 = {"f": 5}

chain = ChainMap(dict1, dict2)

print(chain.maps)

print(chain.keys())  # 返回所有的键

print(chain.values())  # 返回第一个值

chain.new_child()

ct = Counter('abracdaaasdasdf')
ct.update('aaaaaazzzzzz')

print(ct)

"""
UserDict 需要继承写子类然后来使用
"""


class StrDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


##################mappingproxy###################

from types import MappingProxyType
"""
➊ d 中的内容可以通过 d_proxy 看到。
➋ 但是通过 d_proxy 并不能做任何修改。
➌ d_proxy 是动态的，也就是说对 d 所做的任何改动都会反馈到它上面。
"""
d = {1: 'A'}

d_proxy = MappingProxyType(d)  # 只能读取，不能修改


d[2] = "b"  # 可以在原字典上进行修改

############## set ############################
"""
集合用于去重
a b 两个集合  a & b 交集 a|b 合集 a-b 差集
"""
l = ['spam', 'spam', 'eggs', 'spam']

set(l)

# 例子求a b 中重复的次数

a = {'a', 'b', 'c', 'd'}

b = {'c', 'd', 'c'}

found = len(set(a) & set(b))

# 空集合用set() 不能用{} ---字典

# 集合常用的方法：
a.discard('a') # 若存在a则移除
a.isdisjoint(b) # b和a是否有交集
a.pop()
a.add('a')
a.remove('a')  # 从 a 中移除 'a' 元素，若 a 元素不存在，则抛出 KeyError 异常

"""
dict的实现：
01. 键必须是可散列的
    一个可散列的对象必须满足以下要求。
    (1) 支持 hash() 函数，并且通过 __hash__() 方法所得到的散列值是不变的。
    (2) 支持通过 __eq__() 方法来检测相等性。
    (3) 若 a == b 为真，则 hash(a) == hash(b) 也为真。
02. 字典在内存上的开销巨大
    由于字典使用了散列表，而散列表又必须是稀疏的，这导致它在空间上的效率低下。
    举例而言，如果你需要存放数量巨大的记录，那么放在由元组或是具名元组构成的列
    表中会是比较好的选择；最好不要根据 JSON 的风格，用由字典组成的列表来存放这
    些记录。用元组取代字典就能节省空间的原因有两个：其一是避免了散列表所耗费的
    空间，其二是无需把记录中字段的名字在每个元素里都存一遍。
03. 键查询很快
    dict 的实现是典型的空间换时间：字典类型有着巨大的内存开销，但它们提供了无
    视数据量大小的快速访问——只要字典能被装在内存里。正如表 3-5 所示，如果把字
    典的大小从 1000 个元素增加到 10 000 000 个，查询时间也不过是原来的 2.8 倍，从
    0.000163 秒增加到了 0.00456 秒。这意味着在一个有 1000 万个元素的字典里，每秒
    能进行 200 万个键查询。
04. 键的次序取决于添加顺序
    当往 dict 里添加新键而又发生散列冲突的时候，新键可能会被安排存放到另一个位
    置。于是下面这种情况就会发生：由 dict([key1, value1), (key2, value2)]
    和 dict([key2, value2], [key1, value1]) 得到的两个字典，在进行比较的时
    候，它们是相等的；但是如果在 key1 和 key2 被添加到字典里的过程中有冲突发生
    的话，这两个键出现在字典里的顺序是不一样的。
"""


"""
集合里的元素必须是可散列的。
集合很消耗内存。
可以很高效地判断元素是否存在于某个集合。
元素的次序取决于被添加到集合里的次序。
往集合里添加元素，可能会改变集合里已有元素的次序。
"""






