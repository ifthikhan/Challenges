#!/usr/bin/env python
# encoding: utf-8

"""
Implement a function to check if a binary tree is balanced. For the purpose of
this question, a balanced tree is defined to be a tree such that the heights of
the 2 subtrees of any node never differ by more than one.
"""

from collections import namedtuple
import unittest


#Node = namedtuple('Node', ['value', 'left', 'right'])

class Node(object):
    def __init__(self, v, left=None, right=None):
        self.left = left
        self.right = right
        self.v = v

    def __str__(self):
        return "{}({}, {})".format(self.v, self.left, self.right)


def check_height(root):
    if root is None:
        return 0

    left_height = check_height(root.left)
    if left_height == -1:
        return -1

    right_height = check_height(root.right)
    if right_height == -1:
        return -1

    height = abs(left_height - right_height)
    if height > 1:
        print left_height, right_height
        print root
        return -1

    return max(left_height, right_height) + 1


def is_balanced(root):
    if check_height(root) == -1:
        return False
    return True


class TestCheckHeight(unittest.TestCase):

    def test_empty_root(self):
        root = None
        self.assertEqual(check_height(root), 0)

    def test_single_node_with_no_children(self):
        root = Node(v=1)
        self.assertEqual(check_height(root), 1)

    def test_unbalanced_tree(self):
        ccl = Node('E')
        bcl = Node('D', left=ccl)
        acl = Node('B', left=bcl)
        acr = Node('C')
        root = Node('A', left=acl, right=acr)
        self.assertEqual(check_height(root), -1)

    def test_balanced_tree_with_diff_1(self):
        bcl = Node('D')
        acl = Node('B', left=bcl)
        acr = Node('C')
        root = Node('A', left=acl, right=acr)
        self.assertEqual(check_height(root), 3)

    def test_complext_balanced_tree(self):
        "http://stackoverflow.com/questions/14596195/check-if-a-binary-tree-is-balanced-big-o"
        fn = Node('F')
        gn = Node('G')
        en = Node('E', left=fn, right=gn)

        dn = Node('D')

        bn = Node('B', left=dn, right=en)

        iin = Node('I')
        hn = Node('H', left=iin)
        cn = Node('C', right=hn)

        root = Node('A', left=bn, right=cn)
        self.assertEqual(check_height(root), -1)




if __name__ == '__main__':
    unittest.main()
