# itertools 学习
import itertools
# natuals = itertools.count(2)

# for n in natuals:
#     print(n)
#  上述代码会一直循环数字

# cs = itertools.cycle("abc")
# for c in cs:
#     print(c)
# 上述代码会一直循环给出的字母

# ns = itertools.repeat("aaa", 8)
# for n in ns:
#     print(n)  重复循环n次

# for c in itertools.chain("abc", "efg"):
#     print(c)
# 以上代码会将多个可迭代对象合并 然后循环出来 

for k, g in itertools.groupby("AaaaBbbbCccc"):
    print(k, list(g))

# 可以这么写

for k, g in itertools.groupby("AaaaBbbbCccc", lambda c:c.upper()):  # 排序规则可以用匿名函数来指定 
    print(k, list(g))
# 以上可以用来将符合特定条件的内容分组

