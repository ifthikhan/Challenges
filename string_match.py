#!/usr/bin/env python

import unittest


def find(pattern, subject):
    if not pattern:
        return -1

    matched_cnt = 0
    i = 0
    for s in subject:
        i += 1
        if s == pattern[matched_cnt]:
            matched_cnt += 1
        else:
            matched_cnt = 0
        if matched_cnt == len(pattern):
            break
    return i - matched_cnt if matched_cnt else -1


class FindTestCase(unittest.TestCase):

    def test_empty_pattern(self):
        self.assertEqual(-1, find("", "trol"))

    def test_empty_subject(self):
        self.assertEqual(-1, find("", "trol"))

    def test_empty_pattern_and_subject(self):
        self.assertEqual(-1, find("", ""))

    def test_find_pattern_true(self):
        self.assertEqual(2, find("go", "algorithm"))

    def test_find_pattern_true_2(self):
        self.assertEqual(2, find("go", "gigoog"))

    def test_find_pattern_true_3(self):
        self.assertEqual(0, find("go", "gogogogogo"))


if __name__ == '__main__':
    unittest.main()
