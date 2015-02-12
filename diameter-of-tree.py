#!/usr/bin/env python
# encoding: utf-8

"""
Compute the diameter of a tree.

Diameter of a Binary Tree:
The diameter of a tree (sometimes called the width) is the number of nodes on
the longest path between two leaves in the tree. The diagram below shows two
trees each with diameter nine, the leaves that form the ends of a longest path
are shaded (note that there is more than one path in each tree of length nine,
but no path longer than nine nodes).

The diameter of a tree T is the largest of the following quantities:

* the diameter of T’s left subtree
* the diameter of T’s right subtree
* the longest path between leaves that goes through the root of T (this can be
    computed from the heights of the subtrees of T)
"""

import unittest
from collections import namedtuple


Node = namedtuple("Node", ["left", "right", "value"])


def height(root):
    """
    Compute the height of the tree. The height should be calculated by provding
    the left or right subtrees.

    :param root: A instance of Node
    :returns: int
    """
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(1 + lheight + rheight, max(ldiameter, rdiameter))



