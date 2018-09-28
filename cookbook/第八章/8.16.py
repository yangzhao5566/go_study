"""
在类中定义多个构造器
"""

import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

## 这样就可以通过类方法来创建一个实例

a = Date.today()


