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

my_list = DoubleLinkedList()
my_list.append(1)
my_list.append(2)

print(my_list.head.next.value)
print(my_list.tail.value)