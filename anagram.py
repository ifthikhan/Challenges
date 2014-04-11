#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def is_anagram(char_dict, word):
    """Return True/False on whether the give word is an anagram.

    The chars in the char dict must be lowercase

    :param char_dict: A dictionary of characters with the char as key
    :type char_dict: dict
    :param word: Word to check
    :type word: str
    :returns: bool
    """
    if not word or not len(char_dict):
        raise ValueError("Empty words or dictionary not allowed")
    if len(char_dict) != len(word):
        return False
    for c in word.lower():
        if c not in char_dict:
            return False
    return True


def find_anagrams(words):
    i = 0
    result = []
    anagramed = {}
    for word in words:
        if anagramed.has_key(word):
            continue
        i += 1
        tmp = [word]
        char_dict = {c: None for c in word}
        for word in words[i:]:
            if is_anagram(char_dict, word):
                tmp.append(word)
                anagramed[word] = None
        if len(tmp) > 1:
            result.append(tmp)
    return result


class TestAngram(unittest.TestCase):

    def test_is_anagram_empty_char_dict(self):
        with self.assertRaises(ValueError):
            is_anagram({}, "hello")

    def test_is_anagram_empty_word(self):
        with self.assertRaises(ValueError):
            is_anagram({"h": None, "e": None}, "")

    def test_is_anagram_empty_params(self):
        with self.assertRaises(ValueError):
            is_anagram({}, "")

    def test_is_anagram_success(self):
        self.assertEqual(True, is_anagram({"h": None, "e": None}, "eh"))

    def test_is_anagram_caseless_success(self):
        self.assertEqual(True, is_anagram({"h": None, "e": None}, "EH"))

    def test_is_anagram_unequal_length(self):
        self.assertEqual(False, is_anagram({"h": None, "e": None, 'l': None, 'l':
                                            None, 'o': None}, "he"))

    def test_find_anagram_empty_words(self):
        self.assertEqual([], find_anagrams([]))

    def test_find_anagram_empty_words(self):
        words = ["star", "mary", "rats", "tars", "army"]
        anagrams = find_anagrams(words)
        print anagrams
        self.assertEqual(2, len(anagrams))


if __name__ == '__main__':
    unittest.main()
