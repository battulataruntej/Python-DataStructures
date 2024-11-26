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
    def reverse(self):
        last_node = None
        middle_node = self.head
        if self._length < 2:
            return self
        while middle_node.next is not None:
            right_node = middle_node.next
            middle_node.next = last_node
            last_node = middle_node
            middle_node = right_node
        self.head , self.tail = self.tail,self.head
        return self

my_list = SingleLinkedList()
my_list.append(3)
my_list.append(2)
my_list.append(1)
my_list.append(9)
my_list.reverse()
print(my_list.head.value)
print(my_list.tail.value)