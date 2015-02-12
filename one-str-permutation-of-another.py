"""
One str permutation of another
"""

import unittest


def is_permutation(main, subject):
    if len(main) != len(subject):
        return False
    main_set = set(main)
    subject_set = set(subject)
    return True if len(main_set.intersection(subject_set)) == len(main) else False


class TestCase(unittest.TestCase):

    def test_is_permutation(self):
        a = range(10)
        b = range(10)
        self.assertTrue(is_permutation(a, b))

    def test_is_permutation_false(self):
        a = range(1, 10)
        b = range(5, 10)
        self.assertFalse(is_permutation(a, b))


if __name__ == '__main__':
    unittest.main()
