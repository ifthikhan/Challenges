#!/usr/bin/env python
# encoding: utf-8

"""
5-9. Suppose an arithmetic expression is given as a tree. Each leaf is an
integer and each internal node is one of the standard arithmetical
operations ( + , − , * , / ). For example, the expression 2 + 3 * 4 + (3 *
4) / 5 is represented by the tree in Figure (see book)(a).
(see book for figure)
(see book for figure) Give an O(n) algorithm for evaluating such an
expression, where there are n nodes in the tree.

- Bonus: Added a draw tree as well.
"""

import math
import unittest
from collections import namedtuple


def compute(operand, operator1, operator2):
    if operand == "+":
        return operator1 + operator2
    elif operand == "-":
        return operator1 - operator2
    elif operand == "*":
        return operator1 * operator2
    elif operand == "/":
        return operator1 / operator2
    else:
        raise ValueError("Unknow operand {}".format(operand))


def get_children(parent):
    l, r = parent.left, parent.right
    children = []
    if l:
        children.append(l)
    if r:
        children.append(r)
    return children


def tree_to_list(root):
    ls = []
    stack = [root]
    while len(stack):
        ls.append([n.val for n in stack])
        children = []
        while len(stack):
            children += get_children(stack.pop(0))
        stack = children
    return ls


def draw_tree(root):
    ls = tree_to_list(root)
    def find_pos_operand(ls):
        for i, l in enumerate(ls):
            if str(l) in "*/+-":
                yield i
    len_of_base = math.pow(2, len(ls) - 1) * 2 - 1
    symbol_agg = []
    left_padding = 0
    divider_padding = 0
    prev_row = None
    for i, row in enumerate(ls):
        left_padding = int(len_of_base / math.pow(2, i + 1))
        tmp = []
        op_pos = find_pos_operand(prev_row)
        if i == 0:
            s = "{}".format(row[0])
            tmp.append(s)

        last_pos = None
        for v1, v2 in zip(row[::2], row[1::2]):
            pos = next(op_pos) if prev_row else 0
            pad = 0
            if last_pos is not None and (last_pos + 1) < pos:
                missing_pairs = pos - last_pos - 1
                unit_per_parent = 2 + divider_padding + divider_padding
                pad = unit_per_parent * missing_pairs
            s = "{}{}{}{}{}".format(" " * pad, v1, " " * divider_padding,
                                    v2, " " * divider_padding)
            tmp.append(s)
            last_pos = pos

        symbol_agg.append("{}{}".format(" " * left_padding, "".join(tmp)))
        divider_padding = left_padding
        prev_row = row
    print "\n".join(symbol_agg)


def eval_tree(root):
    if not root.left or not root.right:
        return root.val
    if root.left:
        ret_left = eval_tree(root.left)
    if root.right:
        ret_right = eval_tree(root.right)
    return compute(root.val, ret_left, ret_right)


if __name__ == '__main__':
    from collections import namedtuple

    Node = namedtuple("Node", ["left", "right", "val"])
    three = Node(left=None, right=None, val=3)
    four = Node(left=None, right=None, val=4)
    m1 = Node(left=three, right=four, val='*')
    five = Node(left=None, right=None, val=5)
    d1 = Node(left=m1, right=five, val='/')

    m2 = Node(left=three, right=four, val='*')
    two = Node(left=None, right=None, val=2)
    a1 = Node(left=two, right=m2, val='+')

    r = Node(left=d1, right=a1, val='+')

    result = eval_tree(r)
    print "Sum of expression = {}".format(result)
    draw_tree(r)



