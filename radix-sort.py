#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Radix sort implementation in python.
"""

import unittest
import math


def _get_digit(num, pos):
    """Return the digit in the given position

    :param num: The number to extract the digits from.
    :param pos: The position of the digit to be extracted
    """
    if pos <= 0:
        raise ValueError()
    d = None
    while pos:
        d = num % 10
        num /= 10
        pos -= 1
    return d


def _num_digits(num):
    """Return the number of digits in a number

    :param num: The number in base 10
    :type num: int
    :returns: int -- The number of digits
    """
    return int(math.ceil(math.log10(num)))


def _max_digits(ls):
    """Return the length of maximum number in the list

    :param ls: List to find the maximum number.
    :type ls: List
    :returns: int
    """
    n = 0
    for item in ls:
        t = _num_digits(item)
        if t > n:
            n = t
    return n


def radix_sort(ls):
    """Sort a list of integers

    :param ls: List of integers
    :type ls: list
    :returns: list -- Sorted list
    """
    if not len(ls):
        return ls
    pos = 1
    max_digits = _max_digits(ls)
    while True:
        buckets = {}
        for item in ls:
            d = _get_digit(item, pos)
            l = buckets.get(d, [])
            l.append(item)
            buckets[d] = l
        i = 0
        ls_ = []
        while len(ls) > len(ls_):
            try:
                ls_ += buckets[i]
            except KeyError:
                pass
            i += 1
        ls = ls_
        if pos == max_digits:
            break
        else:
            pos += 1
    return ls


class TestModule(unittest.TestCase):

    def test_get_digit_first(self):
        self.assertEqual(4, _get_digit(34, 1))

    def test_get_digit_second(self):
        self.assertEqual(3, _get_digit(34, 2))

    def test_get_digit_third(self):
        self.assertEqual(2, _get_digit(234, 3))

    def test_get_digit_invalid_pos_zero(self):
        with self.assertRaises(ValueError):
            _get_digit(24, 0)

    def test_get_digit_invalid_pos_negative(self):
        with self.assertRaises(ValueError):
            _get_digit(234, -1)

    def test_get_digit_invalid_pos_large(self):
            self.assertEqual(0, _get_digit(234, 100))

    def test_radix_sorter_empty_list(self):
        self.assertEqual([], radix_sort([]))

    def xtest_radix_sort_success_single_digit(self):
        self.assertEqual([1, 2, 5], radix_sort([2, 5, 1]))

    def xtest_radix_sort_double_digits(self):
        self.assertEqual([10, 15], radix_sort([15, 10]))

    def test_radix_sort_mixed_digits(self):
        self.assertEqual([2, 24, 45, 66, 75, 90, 170, 802],
                         radix_sort([170, 45, 75, 90, 2, 24, 802, 66]))


if __name__ == '__main__':
    unittest.main()
