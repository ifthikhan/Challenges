"""
Automated tests.
"""

from unittest import TestCase, main

from linkedlist import (Node, reverse_singly_linkedlist_iter,
                        reverse_singly_linkedlist_recursive)


class TestLinkedList(TestCase):
    """
    Test cases to test the linked behaviour.
    """

    def test_value_empty(self):
        with self.assertRaises(TypeError):
            Node()

    def test_value_none(self):
        n = Node(None)
        self.assertIsNone(n.value)

    def test_value(self):
        n = Node(1)
        self.assertEqual(n.value, 1)

    def test_next_none(self):
        n = Node(1)
        self.assertIsNone(n.next)

    def test_next_set_none(self):
        n = Node(1)
        n.next = None
        self.assertIsNone(n.next)

    def test_next_set_invalid(self):
        with self.assertRaises(ValueError):
            n = Node(1)
            n.next = "Hello"

    def test_next(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        self.assertIs(n1.next, n2)


class TestReverseIterativeFunction(TestCase):
    """
    Test cases to test the iterative reversal of the list.
    """

    def setUp(self):
        self.reversal_func = reverse_singly_linkedlist_iter

    def test_reverse_none(self):
        with self.assertRaises(ValueError):
            self.reversal_func(None)

    def test_reverse_single_node(self):
        n1 = Node(1)
        node = self.reversal_func(n1)
        self.assertIs(node, n1)

    def test_reverse_odd(self):
        self._reverse_variable_len(3)

    def test_reverse_even(self):
        self._reverse_variable_len(4)

    def test_reverse_large(self):
        # TODO: Test for max recursion
        self._reverse_variable_len(40)

    def _reverse_variable_len(self, num):
        nodes = []
        previous = None
        for i in range(num):
            current = Node(i)
            if previous:
                previous.next = current
            nodes.append(current)
            previous = current

        n = self.reversal_func(nodes[0])
        for node in reversed(nodes):
            self.assertIs(n, node)
            n = n.next


class TestReverseRecursiveFunction(TestReverseIterativeFunction):
    """
    Test cases to test the recursive reversal of the list.
    """

    def setUp(self):
        self.reversal_func = reverse_singly_linkedlist_recursive


if __name__ == '__main__':
    main()
