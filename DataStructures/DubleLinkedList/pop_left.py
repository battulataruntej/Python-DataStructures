class Node:

    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next= None

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
         self._length -=1
         return self

my_list = DoubleLinkedList()
my_list.append(1)
my_list.append(2)
my_list.pop_left()
print(my_list.head.next)
print(my_list.tail.next)
