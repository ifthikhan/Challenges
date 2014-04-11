#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def is_anagram(main, word):
    """Return True/False on whether the give word is an anagram.

    The chars in the char dict must be lowercase

    :param main: The main word to check against.
    :type main: str
    :param word: Word to check
    :type word: str
    :returns: bool
    """
    me = is_anagram
    if not hasattr(me, 'char_dicts'):
        me.char_dicts = {}
    if not me.char_dicts.has_key(main):
        char_dict = me.char_dicts[main] = {c: None for c in main}
    else:
        char_dict = me.char_dicts[main]

    if not main or not word:
        raise ValueError("Empty words or dictionary not allowed")
    if len(char_dict) != len(word):
        return False
    for c in word.lower():
        if c not in char_dict:
            return False
    return True


def find_anagrams(words):
    """
    Return a list of lists of anagrams for the given word list.

    :param words: Word list
    :type words: list
    :returns: list
    """
    result = []
    while len(words):
        main = words.pop(0)
        tmp = []
        i = 0
        for _ in range(len(words)):
            try:
                word = words[i]
            except IndexError:
                break
            if is_anagram(main, word):
                tmp.append(word)
                words.pop(i)
            else:
                i += 1
        if len(tmp):
            tmp.append(main)
            result.append(tmp)
    return result


class TestAngram(unittest.TestCase):

    def test_is_anagram_empty_char_dict(self):
        with self.assertRaises(ValueError):
            is_anagram("", "hello")

    def test_is_anagram_empty_word(self):
        with self.assertRaises(ValueError):
            is_anagram("he", "")

    def test_is_anagram_empty_params(self):
        with self.assertRaises(ValueError):
            is_anagram("", "")

    def test_is_anagram_success(self):
        self.assertEqual(True, is_anagram("he", "eh"))

    def test_is_anagram_caseless_success(self):
        self.assertEqual(True, is_anagram("he", "EH"))

    def test_is_anagram_unequal_length(self):
        self.assertEqual(False, is_anagram("hello", "he"))

    def xtest_find_anagram_empty_words(self):
        self.assertEqual([], find_anagrams([]))

    def test_find_anagram_empty_words(self):
        words = ["star", "mary", "rats", "tars", "army"]
        anagrams = find_anagrams(words)
        print anagrams
        self.assertEqual(2, len(anagrams))


if __name__ == '__main__':
    unittest.main()
