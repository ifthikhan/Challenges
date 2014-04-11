#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import unittest


def count_identical_pairs(ls):
    """ Return the number of identical pair of elements in the given list.

    :param ls: List of of integers
    :type ls: list
    :returns: int -- Number of identical pairs
    """
    ls = sorted(ls)
    result = 0
    count = 0
    previous = None
    for current in ls:
        if previous != current and count > 1:
            result += math.factorial(count) / math.factorial(2)
            count = 1
        elif previous is None or current == previous:
            count += 1
        previous = current
        if result == 1000000000:
            break
    return result


class TestCountIdentical(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(0, count_identical_pairs([]))

    def test_success(self):
        ls = [3, 5, 6, 3, 3, 5]
        self.assertEqual(4, count_identical_pairs(ls))


if __name__ == '__main__':
    unittest.main()
