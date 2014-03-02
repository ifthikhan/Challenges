#!/usr/bin/env python

"""
Substring search using Rabbin-Karp algorithm
http://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
"""

import unittest


def rrange(stop):
    """
    Return range of values in descending order. Similar to range

    :param stop int: The length of the range.
    """
    return reversed(range(stop))


class RollingHash(object):

    def __init__(self):
        self.hash_val = 0
        self.base = 101
        self.prev_key = None

    def __roll(self, k):
        if len(k) > 1:
            raise ValueError("The key length must be one")
        self.hash_val -= self.base ** (len(self.prev_key) - 1) * ord(self.prev_key[0])
        self.prev_key = self.prev_key[1:]
        self.hash_val *= self.base
        self.hash_val += ord(k)
        self.prev_key = "{}{}".format(self.prev_key, k)
        return self.hash_val

    def __initial(self, key):
        for i, c in zip(rrange(len(key)), key):
            self.hash_val += self.base ** i * ord(c)
        self.prev_key = key
        return self.hash_val

    def __call__(self, key):
        k = str(key)
        if not len(k):
            raise ValueError("Key cannot be empty")
        if self.prev_key:
            return self.__roll(k)
        else:
            return self.__initial(k)


def substr(pattern, text):
    if not len(pattern):
        return -1
    pat_hash = RollingHash()(pattern)
    hasher = RollingHash()
    pat_len = len(pattern)
    tx_hash = hasher(text[:pat_len])
    for i in range(len(text) - pat_len + 1):
        if pat_hash == tx_hash:
            if pattern == text[i:i + pat_len]:
                return i
        next_char = text[pat_len + i]
        tx_hash = hasher(next_char)
    return -1


class RollingHashTestCase(unittest.TestCase):

    def setUp(self):
        self.rolling_hash = RollingHash()

    def test_empty_key(self):
        with self.assertRaises(ValueError):
            self.rolling_hash("")

    def test_key_str(self):
        key = "bad"
        hashed = 1009595
        self.assertEqual(self.rolling_hash(key), hashed)

    def test_key_int(self):
        key = 342
        hashed = 525553
        self.assertEqual(self.rolling_hash(key), hashed)

    def test_rolling_hash(self):
        initial_key = "bad"
        self.assertEqual(self.rolling_hash(initial_key), 1009595)
        subsequent_chars = "rep"
        hashed = [999711, 1031715, 1173227]
        for c, h in zip(subsequent_chars, hashed):
            self.assertEqual(self.rolling_hash(c), h)


class SubstrTestCase(unittest.TestCase):

    def test_empty_pattern(self):
        self.assertEqual(-1, substr("", "trol"))

    def test_empty_subject(self):
        self.assertEqual(-1, substr("", "trol"))

    def test_empty_pattern_and_subject(self):
        self.assertEqual(-1, substr("", ""))

    def test_substr_pattern_true(self):
        self.assertEqual(2, substr("go", "algorithm"))

    def test_substr_pattern_true_2(self):
        self.assertEqual(2, substr("go", "gigoog"))

    def test_substr_pattern_true_3(self):
        self.assertEqual(0, substr("go", "gogogogogo"))

    def test_substr_pattern_true_4(self):
        self.assertEqual(2, substr("glow", "glglow"))


if __name__ == "__main__":
    unittest.main()

