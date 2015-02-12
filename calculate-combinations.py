#!/usr/bin/env python
# encoding: utf-8

import itertools
import unittest


def calculate_combinations(input_seq, target_sum):
    num, seq = 0, input_seq

    # Micro optimisation
    if len(input_seq) == 0:
        return num
    if min(input_seq) > target_sum:
        return num

    for i in reversed(range(1, len(seq) + 1)):
        lt_than_sum = 0
        num_combinations = 0
        for combination in itertools.combinations(seq, i):
            num_combinations += 1
            s = sum(combination)
            if s == target_sum:
                num += 1
            elif s < target_sum:
                lt_than_sum += 1
        if num_combinations == lt_than_sum:
            break
    return num


class CalculateCombinationsTestCase(unittest.TestCase):

    def test_calculate_combinations(self):
        expected = 3
        actual = calculate_combinations([5, 5, 15, 10], 15)
        self.assertEqual(actual, expected)

    def test_calculate_combinations2(self):
        expected = 2
        actual = calculate_combinations([1, 2, 3, 4], 6)
        self.assertEqual(actual, expected)

    def test_calculate_combinations3(self):
        expected = 2
        actual = calculate_combinations([1, 2, 3, 4, 8], 6)
        self.assertEqual(actual, expected)


    def test_calculate_combinations_all_num_greater_than_target_sum(self):
        expected = 0
        actual = calculate_combinations([7, 8, 9, 10], 6)
        self.assertEqual(actual, expected)

    def test_calculate_combinations_a_num_gt_target_sum(self):
        expected = 1
        actual = calculate_combinations([7, 1, 2, 3], 6)
        self.assertEqual(actual, expected)

    def test_calculate_combinations_empty_input(self):
        expected = 0
        actual = calculate_combinations([], 6)
        self.assertEqual(actual, expected)

    def test_calculate_combinations_zero_as_target_sum(self):
        expected = 0
        actual = calculate_combinations([1,2,3], 0)
        self.assertEqual(actual, expected)

    def test_calculate_combinations_zero_as_target_sum_with_zero_in_seq(self):
        expected = 1
        actual = calculate_combinations([1,2,3, 0], 0)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
