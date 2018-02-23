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