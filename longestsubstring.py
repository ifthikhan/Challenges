#!/usr/bin/env python
# encoding: utf-8


import logging
import unittest
import functools


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


"""
Find the longest substring common to the given 2 strings.
"""


def find_longest_common_substring(str1, str2):
    assert isinstance(str1, str) and isinstance(str2, str)
    if not str1 or not str2:
        return ""
    matrix = [[0 for _ in range(len(str2))]
              for _ in range(len(str1))]
    substr = []
    max_len = 0
    last_substr_pos = 0
    for i, c1 in enumerate(str1):
        for j, c2 in enumerate(str2):
            if c1 == c2:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                if matrix[i][j] > max_len:
                    max_len = matrix[i][j]
                    current_substr_pos = i - matrix[i][j] + 1
                    if current_substr_pos == last_substr_pos:
                        substr.append(c1)
                    else:
                        last_substr_pos = current_substr_pos
                        substr = [c1]
    return "".join(substr)


def log_return(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        ret_val = f(*args, **kwargs)
        logging.debug(ret_val)
        print ret_val
        return ret_val


class TestFindLongestCommongSubstring(unittest.TestCase):

    def test_both_strings_empty(self):
        self.assertEqual(find_longest_common_substring("", ""), "")

    def test_if_one_string_is_empty(self):
        self.assertEqual(find_longest_common_substring("lorem", ""), "")
        self.assertEqual(find_longest_common_substring("", "lorem"), "")

    def test_success_substr_in_beginning(self):
        s1 = "sad"
        s2 = "say"
        expected = "sa"
        self.assertEqual(find_longest_common_substring(s1, s2), expected)

    def test_success_substr_in_middle(self):
        s1 = "sad"
        s2 = "bad"
        expected = "ad"
        self.assertEqual(find_longest_common_substring(s1, s2), expected)

    def test_success(self):
        str1 = "aabbcc"
        str2 = "eebbdd"
        expected = "bb"
        self.assertEqual(find_longest_common_substring(str1, str2), expected)


if __name__ == '__main__':
    unittest.main()
