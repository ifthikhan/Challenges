#!/usr/bin/env python
# encoding: utf-8

import unittest


def odd_recursive(in_seq):
    if len(in_seq) is 0:
        return []
    v = in_seq.pop(0)
    return ([v] if v % 2 == 1 else []) + odd_recursive(in_seq[:len(in_seq)]) 


def odd_iter(in_seq):
    out_seq = []
    while len(in_seq):
        v = in_seq.pop(0)
        if v % 2 == 1:
            out_seq.append(v)
    return out_seq


class TestCase(unittest.TestCase):

    def test_recursive(self):
        seq = [1, 3, 4, 2, 9, 15]
        expected = [1, 3, 9, 15]
        actual = odd_recursive(seq)
        self.assertEqual(actual, expected)

    def test_iter(self):
        seq = [1, 3, 4, 2, 9, 15]
        expected = [1, 3, 9, 15]
        actual = odd_iter(seq)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
