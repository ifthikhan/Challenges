"""
Heap related data structure and operations.
"""


class BinaryHeap(object):
    """
    Binary implementation using a list.
    """

    def __init__(self):
        self.__keys = [None]
        self.n = 0

    def insert(self, key):
        self.__keys.append(key)
        self.n += 1
        self.__swim(self.n)

    def del_max(self):
        max_val = self.__keys.pop(1)
        self.__sink(1)
        return max_val

    @property
    def empty(self):
        self.__keys = [None]

    @property
    def max(self):
        return self.__keys[1]

    def __len__(self):
        return self.n

    def __swim(self, index):
        while index > 1 and self.__less(index / 2, index):
            self.__exch(index, index / 2)
            index /= 2

    def __sink(self, index):
        while 2 * index <= self.n:
            j = 2 * index
            if j < self.n and self.__less(j, j + 1):
                j += 1
            if not self.__less(index, j):
                break
            self.__exch(index, j)
            index = j

    def __less(self, i1, i2):
        return self.__keys[i1] < self.__keys[i2]

    def __exch(self, i1, i2):
        tmp = self.__keys[i1]
        self.__keys[i1] = self.__keys[i2]
        self.__keys[i2] = tmp

    def __iter__(self):
        for k in self.__keys[1:]:
            yield k

    def __str__(self):
        return str(self.__keys)

    def __unicode__(self):
        return unicode(self.__keys)
