# 元类的学习  type
# 动态语言和静态语言最大的不同，就是函数和类的定义，
# 不是编译时定义的，而是运行时动态创建的。
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000

# 通过type 创建一个类
def fn(self, name="world"):
    print("hello, %s" % name)

Hello = type("Hello",(object,), dict(hello=fn))

# type 创建一个对象的三个参数 
# class 的名称 ”hello“
# 继承的父类集合， object
# class 的方法名称与函数绑定，传入的是个字典 这里把函数fn绑定到方法名hello上

##########################metaclass 学习##########

# 一个类的创建顺序为 metaclass  创建一个类 然后类实例化生成一个实例
# 所以通过metaclass 可以创建一个类，也可以在类的创建过程中修改一个类
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# ___new__() 方法接收到的参数一次是：
# 当前准备创建的类的对象
# 类的名称
# 类继承的父类集合
# 类的方法集合

class MyList(list, metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L)
