"""
创建缓存实例
"""

import weakref

_spam_cache = weakref.WeakValueDictionary()


class Spam:
    def __init__(self, name):
        self.name = name


def get_sapm(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s

        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class NewSpam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_spam(name):
        return NewSpam.manager.get_spam(name)

