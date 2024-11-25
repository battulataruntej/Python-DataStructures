class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length=0

    def append(self,value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length +=1
        return self
    def prepend(self,value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length +=1
        return self
    def pop_left(self):
        if not self._length > 1:
            self.head = self.tail = None
        else:
            tmp = self.head.next
            self.head.next = None
            self.head = tmp
        self._length -=1
        return self


my_list=SingleLinkedList()
print(my_list)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.prepend(1)
print(my_list.head.value)
print(my_list.tail.value)