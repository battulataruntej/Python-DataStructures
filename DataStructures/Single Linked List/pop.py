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
    def pop_left(self):
        if not self._length > 1:
            self.head = self.tail = None
        else:
            tmp = self.head.next
            self.head.next = None
            self.head = tmp
        self._length -=1
        return self

    def pop_left2(self):
        if not self._length:
            raise Exception("list is empty")
        former_head=self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail =None
        return self

my_list = SingleLinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.pop_left2()
my_list.pop_left2()
my_list.pop_left2()
print(my_list.head.value)
print(my_list.tail.value)