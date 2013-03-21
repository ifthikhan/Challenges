"""
Automated tests.
"""

from unittest import TestCase, main

from singlylinkedlist import Node, SinglyLinkedList


class TestLinkedList(TestCase):
    """
    Test cases to test the Node.
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

    def test_node_equal(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2

        n3 = Node(1)
        n4 = Node(2)
        n3.next = n4
        self.assertEqual(n1, n3)

    def test_node_strr(self):
        n = Node(1)
        self.assertEqual(str(n), str(1))

    def test_node_repr(self):
        n = Node(1)
        n2 = Node(2)
        n.next = n2
        self.assertEqual(repr(n),
                         "Node({}, {})".format(repr(n.value), repr(n.next)))


class TestSinglyLinkedList(TestCase):
    """
    Test cases to test the collection wrapper
    """

    def setUp(self):
        self.sll = SinglyLinkedList()
        self.reverse = getattr(self.sll, 'reverse_iterative')

    def test_empty_list(self):
        self.assertEqual(len(self.sll), 0)

    def test_list_single_item(self):
        self.sll.append(1)
        self.assertEqual(len(self.sll), 1)
        for v in self.sll:
            self.assertEqual(v, 1)

    def test_list_multi_items(self):
        num = 10
        for i in range(num):
            self.sll.append(i)

        for i, list_val in zip(range(num), self.sll):
            self.assertEqual(i, list_val)

    def test_to_str(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.assertEqual(str(self.sll), str([1, 2, 3]))

    def test_to_repr(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.assertEqual(repr(self.sll), "{}({})".format("SinglyLinkedList",
                                                         repr([1, 2, 3])))


class SinglyLinkedListReverse(object):
    """
    Abstract class to group all the common tests to test the reverse
    feature.
    """

    def _populate_sll(self, num_vals):
        for i in range(num_vals):
            self.sll.append(i)

    def test_reverse_empty_list(self):
        self.reverse()

    def test_reverse_single_item(self):
        self.sll.append(1)
        self.reverse()
        self.assertEqual(1, next(iter(self.sll)))

    def test_reverse_multi_items(self):
        num = 10
        self._populate_sll(num)
        self.reverse()

        for i, list_val in zip(reversed(range(num)), self.sll):
            self.assertEqual(i, list_val)

    def test_reverse_multi_items_large(self):
        num = 400
        self._populate_sll(num)
        self.reverse()

        for i, list_val in zip(reversed(range(num)), self.sll):
            self.assertEqual(i, list_val)


class TestSinglyLinkedListReverseIterative(TestCase, SinglyLinkedListReverse):

    def setUp(self):
        self.sll = SinglyLinkedList()
        self.reverse = getattr(self.sll, 'reverse_iterative')


class TestSinglyLinkedListReverseRecursive(TestCase, SinglyLinkedListReverse):

    def setUp(self):
        self.sll = SinglyLinkedList()
        self.reverse = getattr(self.sll, 'reverse_recursive')


if __name__ == '__main__':
    main()
