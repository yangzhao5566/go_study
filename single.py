# 单例模式
from functools import wraps

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# 导入模块即是一种天然的单例 

#  继承父类的方式 super(Singleton, cls).__new__(cls, *args, **kwargs) 
# super(B, self).__init(self, *args, *kwargs)

# 使用functools 中的 wraps 来完成单例

def Singleton2(cls):
    instance = {}
    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance
    return getinstance

@Singleton2
class MyClass(object):
    a = 1


# 使用metaclass
class Singleton3(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton3, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
# 使用 py2
class MyClass(object):
    __metaclass__ = Singleton3

# py3 
class MyClass(metaclass=Singleton3):
    pass
#  总结下 元类的作用：
# 拦截类的创建
# 修改类的定义
# 返回修改后的类



####################### 
# 顺带看下闭包

def test(func):
    @wraps(func)
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print("before")
        return func(*args, **kwargs)
    return call_it

@test
def hello():
    print("hello ")