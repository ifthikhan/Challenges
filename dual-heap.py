"""
Create a binary heap for min and max values of inputs with the following
interface
    - add
    - delete
    - get
    - size
"""

import abc
import unittest

class BinaryHeap(object):

    #__meta__ = abc.ABCMeta

    def __init__(self):
        self._vals = []

    def __len__(self):
        return len(self._vals)

    def add(self, v):
        self._vals.append(v)
        self._swim()

    def get(self):
        last = len(self) - 1
        self._exch(0, last)
        ret_val = self._vals.pop(last)
        self._sink()
        return ret_val

    def peek(self):
        return self._vals[0]

    def _sink(self):
        """Push the root down to satisfy the heap property"""
        parent_ix = 0
        left_ix, right_ix = self._get_children_ixs(parent_ix)
        while left_ix or right_ix:
            if left_ix and right_ix:
                to_exch = self._select_child(left_ix, right_ix)
            elif left_ix:
                to_exch = left_ix
            else:
                to_exch = right_ix
            self._exch(parent_ix, to_exch)
            parent_ix = to_exch
            left_ix, right_ix = self._get_children_ixs(parent_ix)

    def _swim(self):
        """Inspect and promote the last element to satisfy the heap property"""
        child_ix = len(self) - 1
        parent_ix = self._get_parent(child_ix)
        while (parent_ix is not None and self._test(parent_ix, child_ix)):
            self._exch(parent_ix, child_ix)
            child_ix = parent_ix
            parent_ix = self._get_parent(parent_ix)

    def _exch(self, ix_1, ix_2):
        """Exchange the values of the given indices

        :param int ix_1     First index
        :param int ix_2     Second index
        """
        tmp = self._vals[ix_1]
        self._vals[ix_1] = self._vals[ix_2]
        self._vals[ix_2] = tmp

    def _get_parent(self, child_ix):
        """Return the parent for a given child. If child is root returns None.

        :param int child_ix
        """
        if child_ix == 0:
            return None
        t = 1 if child_ix & 1 else 2
        return (child_ix - t) / 2

    def _get_children_ixs(self, parent_ix):
        """Return the indices of the children. None if out of bounds

        :param int parent_ix    The parent index
        """
        ix_left = (parent_ix * 2) + 1
        ix_right = ix_left + 1
        if ix_left >= len(self):
            ix_left = None
        if ix_right >= len(self):
            ix_right = None
        return ix_left, ix_right

    @abc.abstractmethod
    def _test(self, v1_ix, v2_ix):
        raise NotImplementedError

    @abc.abstractmethod
    def _select_child(self, child1_ix, child2_ix):
        raise NotImplementedError

    def __str__(self):
        return "{}".format(" ".join(self._vals))


class MaxBinaryHeap(BinaryHeap):

    def _test(self, parent_ix, child_ix):
        return self._vals[parent_ix] < self._vals[child_ix]

    def _select_child(self, child1_ix, child2_ix):
        if self._test(child2_ix, child1_ix):
            return child1_ix
        else:
            return child2_ix


class MinBinaryHeap(BinaryHeap):

    def _test(self, parent_ix, child_ix):
        return self._vals[parent_ix] > self._vals[child_ix]

    def _select_child(self, child1_ix, child2_ix):
        if self._test(child2_ix, child1_ix):
            return child1_ix
        else:
            return child2_ix


class BinaryHeapTestBase(object):

    def test_add_initialization(self):
        self.assertEqual(len(self.h), 0)

    def test_add(self):
        self.h.add(1)
        self.assertEqual(len(self.h), 1)

    def test_get(self):
        self.h.add(2)
        self.assertEqual(2, self.h.get())
        self.assertEqual(len(self.h), 0)

    def test_peek(self):
        self.h.add(1)
        self.assertEqual(1, self.h.peek())
        self.assertEqual(len(self.h), 1)


class MaxBinaryHeapTestCase(unittest.TestCase, BinaryHeapTestBase):

    def setUp(self):
        self.h = MaxBinaryHeap()

    def test_heap_value_top(self):
        self.h.add(1)
        self.h.add(2)
        self.assertEqual(2, self.h.get())

    def test_heapify(self):
        self.h.add(1)
        self.h.add(2)
        self.assertEqual(2, self.h.peek())
        self.h.add(10)
        self.assertEqual(10, self.h.peek())
        self.h.add(20)
        self.assertEqual(20, self.h.peek())
        self.h.add(12)
        self.assertEqual(20, self.h.peek())

    def test_heapify_after_get(self):
        self.h.add(7)
        self.h.add(5)
        self.h.add(6)
        self.h.add(1)
        self.assertEqual(7, self.h.get())
        self.assertEqual(6, self.h.get())
        self.assertEqual(5, self.h.get())


class MinBinaryHeapTestCase(unittest.TestCase, BinaryHeapTestBase):

    def setUp(self):
        self.h = MinBinaryHeap()

    def test_heap_value_top(self):
        self.h.add(2)
        self.h.add(1)
        self.assertEqual(1, self.h.get())

    def test_heapify(self):
        self.h.add(10)
        self.h.add(7)
        self.assertEqual(7, self.h.peek())
        self.h.add(10)
        self.assertEqual(7, self.h.peek())
        self.h.add(6)
        self.assertEqual(6, self.h.peek())
        self.h.add(5)
        self.assertEqual(5, self.h.peek())

    def test_heapify_after_get(self):
        self.h.add(1)
        self.h.add(6)
        self.h.add(5)
        self.h.add(7)
        self.assertEqual(1, self.h.get())
        self.assertEqual(5, self.h.get())
        self.assertEqual(6, self.h.get())

if __name__ == "__main__":
    unittest.main()
