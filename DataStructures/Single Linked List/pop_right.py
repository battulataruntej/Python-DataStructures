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
    def pop_right(self):
        if not self._length:
            raise Exception("Nothing to do as it is a Empty.!")
        if self._length==1:
            self.head = self.tail = None
        tmp_head = self.head
        while tmp_head.next is not self.tail:
            tmp_head = tmp_head.next
        self.tail = tmp_head
        self.tail.next =None
        self._length-=1
        return self
my_list=SingleLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.pop_right()
print(my_list.head.value)
print(my_list.tail.value)