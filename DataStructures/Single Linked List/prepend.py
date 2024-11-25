class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self._length=0

    def prepend(self,value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length +=1
        return self


my_list=SinleLinkedList()
my_list.prepend(2)
my_list.prepend(3)
my_list.prepend(1)
print(my_list.head.value)
print(my_list.tail.value)
