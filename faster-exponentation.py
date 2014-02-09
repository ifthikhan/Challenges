#!/usr/bin/env python

"""
Faster exponentation using the following formular:
Even exponents = a^n = (a ^ n/2)^2
Odd exponents = a((a^n/2)^2)
"""

import unittest

def fast_exp(base, exp):
    if base == 0:
        return 0
    result = 1
    for _ in range(exp / 2):
        result *= base
    result = result * result
    if exp & 1:
        result *= base
    return result


class FastExpTestCase(unittest.TestCase):

    def test_success(self):
        self.assertEqual(8, fast_exp(2, 3))

    def test_zero_exp(self):
        self.assertEqual(1, fast_exp(2, 0))

    def test_zero_base(self):
        self.assertEqual(0, fast_exp(0, 1))

    def test_zero_base_and_exp(self):
        self.assertEqual(0, fast_exp(0, 0))


if __name__ == '__main__':
    unittest.main()

