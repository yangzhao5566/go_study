# coding=utf8

"""
容器序列
list tuple collections.deque 这些序列能存放不同的类型的数据
扁平序列：
srt bytes bytearray memoryview array.array 这类序列只能荣南一中类型
容器序列存放的是他们所包含的任意类型的对象的引用。而扁平序列里存放的是值而不是引用换句话说
扁平序列其实是一段连续的内存管空间

可变序列：
    list, bytearray array.array collections.deque memoryview

不可变序列：
tuple str bytes
"""

##########列表推导式################

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

##############py2 or py3###########
"""
在py2中for循环之后的复制操作可能会影响列表推导上下文中的同名变量
py3中则不会

在python3中你可以这样写
x = 'ABC'
dummy = [ord(x) for x in x]
➊ x 的值被保留了。
➋ 列表推导也创建了正确的列表。
"""
x = 'ABC'
dummy = [ord(x) for x in x]


#############filter && map ########3

bey_ascii = [ord(s) for s in symbols if ord(s) > 127]

bey_ascii = list(filter(lambda c: c > 127, map(ord, symbols))) #执行顺序从右向左



#########笛卡尔积#####################

colors = ['black', 'white']

sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

###############列表生成式#############
"""
列表生成式的好处在于可以逐个的产出元素，而不是建立一个完整的列表
"""

import array

tuple(ord(symbol) for symbol in symbols)

array.array('I', (ord(symbol) for symbol in symbols))


for tshirt in ('%s %s'%(c, s) for c in colors for s in sizes):
    print(tshirt)



#######################元组###############
"""
元组不仅可以作为不可变的列表还可以用于没有字段名的记录
"""

# 把元组用作记录

lax_coordinates = (33.9425, -118.408056)

print("%s/%s" % lax_coordinates)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for country, _ in traveler_ids:
    print(country)


##################元祖拆包####################
latitude, longitude = lax_coordinates

a, b = 1, 2

a, b = b, a

divmod(20, 8)

t = (20, 8)
divmod(*t)  #进行拆包

import os

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

"""
* 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的
任意位置
"""
c, d, *rest = range(5) # *rest 返回的是个列表


metro_areas = [
 ('Tokyo','JP',36.933,(35.689722,139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: # 对于元祖还可以这样解包
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))



################具名元组######################

from collections import namedtuple

City = namedtuple("City", 'name country population coordinates')

"""
创建一个具名元组需要两个参数，一个是类名， 一个是类的各个字段的名字。后者可以是数个字符串组成
可迭代对象，或者是由空格分隔开的字段组成的字符串
"""
tokyo = City('Tokyo', 'JP',  36.933, (35.689722, 139.691667))

"""
可以通过字段名或者位置来获取一个字段的的信息"""

tokyo[1] # 支持下标的方式来取值
tokyo.name

"""除了从普通元祖哪里集成来的属性外，还有自己的转悠属性
   _fields 类属性，类方法 _make(iterable) 和实例方法_adict()
"""

City._fields # 返回所有的字段名称的元祖

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data) # 把可迭代对象生成一个具名元组和 City(*delhi_data)作用一样的

delhi._asdict() # 把具名元组以collections.OrderedDict 形式返回




#############作为不可变列表的元组####################

"""
__add__  拼接  __iadd__ 就地拼接

"""

###############切片部位人知的方法####################
"""
列表元祖字符串都支持切片
"""


invoice = """
0.....6................................40........52...55........
1909 Pimoroni PiBrella              $17.50 3 $52.50
1489 6mm Tactile Switch             x20 $4.95 2 $9.90
1510 Panavise Jr. - PV-201          $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240         $34.95 1 $34.95
"""

SKU = slice(0, 6)

DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])



##########给切片赋值#############

l = list(range(10))

"""
赋值后还是一个列表
如果赋值对象是一个切片，那么赋值语句的右侧必须是个可迭代对象
"""
l[2:5] = [20, 40]


################序列使用+ or *###################3
"""
+ 两侧的序列由相同的数据类型构成，在拼接的过程中，两个被操作的序列都不会被修改，
python会新建一个包含同样类型数据的序列来作为拼接的结果
"""

l = [1, 2, 3]

m = l * 5

print(id(l), id(m))

n = 'abcd'
o = 5 * n

"""+ 和 * 都遵循这个规律，不修改原有的操作对象，而是构建一个全新的序列 """

"""变量的引用"""
board = [['_'] * 3 for i in range(3)]

board[1][2] = 'X'


"""错误的引用"""

weird_board = [['_'] * 3] * 3

weird_board[1][2] = 'X'

print(weird_board, board)



#################+= or *= ######################
"""
+= 背后的特殊方法是__iadd__ 就地加法 若没实现这个方法则会退一步调用__add__
a += b 若a实现了__iadd__ 方法，就会调用这个方法，对于可变序列 来说，a就会就地改动，就像
调用a.extend(b) 一样。
但是若未实现__iadd__  a+=b 表达式的效果就会跟 a = a + b 一样将返回一个新的对象 重新赋值给
a
"""

print(id(l))

l *= 2

print(id(l))

t = (1, 2, 3)

print(id(t))

t *= 2

print(id(t))

"""
对于不可变序列进行重复拼接操作，效率会很低，因为每次都要有一个新的对象
把原来的对象中的元素复制到新的对象里，在追加新的元素（str除外 做了优化)
"""


####################排序#######################
"""list.sort() 方法为就地排序， 不会把元列表赋值一份 这个方法的返回值为None
    与内置函数sorted 不同，他会新建一个列表作为返回值，这个方法可以接受任何形式的可迭代对象
    作为参数，包括不可变序列和生成器 不管接受怎样的参数，都会返回一个列表
"""

"""
sorted的用法： key 一个只有一个参数的函数函数的参数为列表里的元素，
这个函数会被用在序列里的每一个元素上。所产生的
结果将是排序算法依赖的对比关键字
"""


############## bisect ####################
"""bisect 二分查找到的一个实现
bisect.insort() 在一个已经排序的数组里边插入一个新的数据
"""
import bisect

data = [4, 2, 9, 7]
data.sort()

bisect.insort(data, 3)

"""
bisect.bisect(data, 1) 只会查找该数值将会插入的位置并返回，而不会插入
"""
bisect.bisect(data, 1)


bisect.bisect_left(data, 4)  # 不插入只返回位置
bisect.bisect_right(data, 4)    # 同上

bisect.insort_left(data, 4)
bisect.insort_right(data, 4)


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


"""
列表虽然灵活，但面对不同需求的时候不一定是最好的选择， 要存放大数量浮点数的话，用array模块
显然会更好，如果需要频繁对序列做先进先出操作，deque的速度会更快
如果检查一个元素是否出现在一个集合中，set会更合适，set专为检查元素做过优化
"""

#############数组#######################

"""
array.array 比list更高效， 数组支持所有的尅版序列的操作，.pop .insert .exteng 另外
数组还提供从文件读取和存入文件的更快的方法 .frombytes  .tofile等
"""

# 创建数组需要一个类型码， 这个类型码用来表示在底层的c应该怎么存放的数据类型
# b类型码表示的是有符号的字符串 可以存放一个字节大小的整数。 -128 - 127

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# 从文件读取

floats2 = array('d')
fp = open('floats.bin', 'rb')

floats2.fromfile(fp, 10**7)

fp.close()

# floats == floats2  可以用来判断是否是相等


#############双向队列#################

from collections import deque

dq = deque(range(10), maxlen=10)

dq.appendleft(-1) # 在最左边添加

dq.extendleft([-1, -20, -9])

dq.rotate(2)