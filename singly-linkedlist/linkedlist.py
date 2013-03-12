"""
Implementation of singly linked list
"""


class Node(object):
    """
    Represent a single element in the list
    """

    __slots__ = ['_value', '_next']

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

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
        return str(self.value)

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   repr(self.value),
                                   repr(self.next))

    def __eq__(self, other):
        return self.value == other.value and self.next == other.next


class SinglyLinkedList(object):
    """
    The collection wrapper.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next
        self.length += 1

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __len__(self):
        return self.length

    def __to_list(self):
        plist = []
        for i in self:
            plist.append(i)
        return plist

    def __str__(self):
        return "{}".format(self.__to_list())

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, repr(self.__to_list()))

    def reverse_iterative(self):
        """
        Reverse the list iteratively and in-place
        """
        if len(self) == 0:
            return
        new_head = _reverse_singly_linkedlist_iter(self.head)
        self.tail = self.head
        self.head = new_head

    def reverse_recursive(self):
        """
        Reverse the list recursively and in-place
        """
        if len(self) == 0:
            return
        new_head = _reverse_singly_linkedlist_recursive(self.head)
        self.tail = self.head
        self.head = new_head


def _reverse_singly_linkedlist_iter(node):
    """
    Reverses the given singly linked list iteratively.
    :param Node node: The sentinel node
    """
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


def _reverse_singly_linkedlist_recursive(node):
    """
    Reverses the given singly linked list recursively.
    :param Node node: The sentinel node
    """
    if not node.next:
        return node

    nxt = _reverse_singly_linkedlist_recursive(node.next)
    node.next.next = node
    node.next = None
    return nxt
