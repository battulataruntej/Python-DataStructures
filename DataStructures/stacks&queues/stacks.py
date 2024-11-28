class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class stack:

    def __init__(self):
        self._top = None
        self._size = 0
        self._max_allowed_elements = 10

    def __len__(self):
        return self._size

    def push(self, value):
        if self._size == self._max_allowed_elements:
            raise Exception("We have exceeded the limit")
        new_element = Node(value)
        new_element.next = self._top
        self._top = new_element
        self._size += 1
        return self

    def pop(self):
        if not self._size:
            raise Exception(" Hey There are no elements to pop ..!")
        former_head = self._top
        self._top = former_head.next
        former_head.next = None
        self._size -= 1
        return former_head.value

    def peek(self):
        return self._top if self._size else None

    def clear(self):
        self._top = None
        self._size = 0
        return self

my_list = stack()
my_list.push(1)
my_list.push(2)
my_list.push(3)
print(len(my_list))


