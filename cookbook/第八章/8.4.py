"""
创建大量对象时节省内存方法
"""


class Date:
    __slots__ = ["year", "month", "day"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

"""
当你定义__slots__ 后，Python就会为实例使用一种更加紧凑的内部表示。 实例通过一个很小
的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。 在 __slots__ 
中列出的属性名在内部被映射到这个数组的指定小标上。 使用slots一个不好的地方就是我们不能再给
实例添加新的属性了，只能使用在 __slots__ 中定义的那些属性名。
"""