
class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

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

    def pop_left(self):
        if not self._length:
            raise Exception("Its a Empty list .! ")
        if self._length == 1:
            self.head = self.tail = None
        else:
            other = self.head.next
            self.head.next = None
            self.head = other
        self.head.prev = None
        self._length -= 1
        return self

    def pop_right(self):
        if not self._length:
            raise Exception("Its a Empty list")
        if self._length == 1:
            self.head = self.tail = None
        else:
            tmp = self.tail.prev
            self.tail.prev = None
            self.tail = tmp
            self.tail.next = None
        self._length -= 1
        return self
    def remove(self,value):
        if not self._length:
            raise Exception("List is Empty")
        if self.head.value == value:
            return self.pop_left()
        prev_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("Invalid input Value")
        if current_node.next is None:
            return self.pop_right()
        current_node.next.prev = prev_node
        prev_node.next = current_node.next
        current_node.next = None
        current_node.prev = None
        self._length -= 1
        return current_node.value


my_list = DoubleLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.remove(8)
print(my_list._length)
print(my_list.head.value)
print(my_list.tail.value)
