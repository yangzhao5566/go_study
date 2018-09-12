"""
Bag
"""


class Bag(object):
    """
    bag
    """
    def __init__(self):
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, "item must in the bag"
        return self._items.remove(item)

    def __iter__(self):
        return _BagIterator(self._items)


class _BagIterator(object):
    def __init__(self, seq):
        self._bag_items = seq
        self._cur_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_item < len(self._bag_items):
            item = self._bag_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration


