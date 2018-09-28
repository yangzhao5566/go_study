"""
属性的代理访问
"""

class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, item):
        """
        getattr 只有在访问不到属性的时候才会调用
        :param item:
        :return:
        """
        return getattr(self._a, item)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print("getattr:", item)

    def __setattr__(self, key, value):
        if key.startswith("_"):
            super().__setattr__(key, value)
        else:
            print("setattr:", key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith("_"):
            super().__delattr__(item)

        else:
            print("delattr:", item)
            delattr(self._obj, name)






