"""
Implementation of singly linked list
"""


class Node(object):
    """
    Represent a single element in the list
    """

    __slots__ = ['_value', '_next']

    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        """
        Returns the value of the node
        """
        return self._value

    @property
    def next(self):
        """
        Returns the next node. If this is the last node a None will be returned
        """
        return self._next

    @next.setter
    def next(self, next_node):
        """
        Set the next node. Raises a ValueError if the node set is not of type
        Node or None
        :param Node next_node: The next node.
        """
        if next_node is None or isinstance(next_node, (Node)):
            self._next = next_node
        else:
            raise ValueError("next_node should be of type Node or None")

    def __str__(self):
        return "<Node value={}>".format(self.value)


def reverse_singly_linkedlist_iter(node):
    """
    Reverses the given singly linked list iteratively.
    :param Node node: The sentinel node
    """
    if not isinstance(node, Node):
        raise ValueError("node should be of type Node")

    if node.next is None:
        return node

    nxt = node.next
    node.next = None
    while True:
        nxtnxt = nxt.next
        nxt.next = node
        node = nxt
        nxt = nxtnxt
        if not nxtnxt:
            break
    return node


def reverse_singly_linkedlist_recursive(node):
    """
    Reverses the given singly linked list recursively.
    :param Node node: The sentinel node
    """
    if not isinstance(node, Node):
        raise ValueError("node should be of type Node")

    if not node.next:
        return node

    nxt = reverse_singly_linkedlist_recursive(node.next)
    node.next.next = node
    node.next = None
    return nxt
