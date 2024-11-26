class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1
        return self

my_list = DoubleLinkedList()
my_list.append(1)
print(my_list.head.prev)
print(my_list.tail.next)
