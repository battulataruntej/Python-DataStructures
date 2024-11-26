class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
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
            self.tail = new_node
        self._length += 1
        return self

    def pop_left(self):
        if not self._length > 1:
            self.head = self.tail = None
        else:
            tmp = self.head.next
            self.head.next = None
            self.head = tmp
        self._length -= 1
        return self

    def remove(self, value):
        if not self._length:
            raise Exception("List is Empty")
        if self.head.value == value:
            return self.pop_left()
        prev_node = self.head
        current_node = prev_node.next
        while current_node.value != value:
            prev_node = current_node
            current_node = prev_node.next
        if current_node.next is None:
            self.tail = prev_node
        prev_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node.value


my_list = SingleLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.remove(1)
print(my_list.head)
print(my_list.tail)
