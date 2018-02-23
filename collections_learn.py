# collections 模块学习
from collections import namedtuple
from functools import partial
from collections import deque
from collections import OrderedDict
from collections import defaultdict
from collections import Counter

point = namedtuple("Point", ["x", "y"]) # 创建一个具名元组
p2 = partial(point, x="2")
pp = p2(y=3)
p = point(1, 2)
print(pp.x)
print(p.x)
print(p.y)

q = deque(["a", "b", "c"])
q.append("x")
q.appendleft("y")
# 除此之外还有 pop popleft

# defaultdict  给字典设置默认值

dd = defaultdict(lambda: "MB")
dd["key1"] = "abc"
print(dd["key"]) # 此时没有赋值会返回默认值 “MB"

d = dict([("a",1), ("b", 2), ("c", 3)]) # 此时的字典是无须的

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)]) # 这时候的字典是有序字典


# 简单计数器 Counter

c = Counter()

for ch in "programming":
    c[ch] = c[ch] + 1

print(c)
