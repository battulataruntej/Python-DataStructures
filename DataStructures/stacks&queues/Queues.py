class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, value):
        new_node = Node(value)
        if not self._size:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return self
    def dequeue(self):
        if not self._size:
            raise Exception("Hey It seems to be Empty list")
        tmp = self.head
        if tmp.next is None:
            self.head = self.tail = None
        self.head = tmp.next
        tmp.next = None
        self._size -= 1
        return tmp.value


my_list = queue()
my_list.enqueue(1)


my_list.dequeue()
print(my_list.head)
print(my_list.tail)