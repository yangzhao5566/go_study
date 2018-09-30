"""
利用Mixins 扩展类功能
"""
from collections import defaultdict


class LoggedMappingMixin:
    __slots__ = ()  # 混入类没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, item):
        print("Getting" + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("Deleting" + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + " already set")
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("keys must be strings")
        return super().__setitem__(key, value)


"""
以上的类单独使用起来没有任何意义，事实上如果你去实例化任何一个类
"""


class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()
d["x"] = 12


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = SetOnceDefaultDict(list)
d["x"].append(2)
d["x"].append(3)


#### 通过装饰器来实现


def LoggedMapping(cls):
    """使用装饰器来实现"""
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print("'Getting ' + str(key)")
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__


@LoggedMapping
class LoggedDict(dict):
    pass
















