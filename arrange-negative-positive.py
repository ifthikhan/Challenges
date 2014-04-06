#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

"""
Give an efficient algorithm to rearrange an array of n keys so that all the
negative keys precede all the nonnegative keys. Your algorithm must be
in-place, meaning you cannot allocate another array to temporarily hold the
items. How fast is your algorithm?
"""

def sorter(ls):
    high = len(ls) - 1
    low = 0
    while low < high:
        if ls[low] > 0 and ls[high] < 0:
            swap(ls, low, high)

        if ls[low] < 0:
            low += 1
        if ls[high] > 0:
            high -= 1
    return ls


def swap(ls, i, j):
    tmp = ls[i]
    ls[i] = ls[j]
    ls[j] = tmp


class SorterTestCase(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual([], sorter([]))

    def test_success(self):
        self.assertEqual([-1, -3, -4, 5, 1, 2], sorter([-1, 2, -4, 5, 1, -3]))

    def test_odd_num_list(self):
        self.assertEqual([-1, -4, -3, 1, 5], sorter([-1, -4, 5, 1, -3]))


if __name__ == '__main__':
    unittest.main()
