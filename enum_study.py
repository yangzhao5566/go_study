# 学习 enum
from enum import Enum
from enum import unique  # 装饰器用来检查保证没有重复值

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Tue.value)


# 或者这样用
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 
'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)   # 其中的value 值是自动赋给成员的 从1开始

for k, v in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
    print(k, v)
