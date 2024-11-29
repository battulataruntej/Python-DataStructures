class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        current_node = self.root
        while value != current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self

    def contains(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def remove(self, value, start = None,parent = None):
        current_node = self.root
        while current_node and value != current_node.value:
            parent = current_node
            if value < current_node.value:
                current_node = parent.left
            else:
                current_node = parent.right
        if not current_node:
            raise Exception("Item Not in the tree")
        if not current_node.left and not current_node.right:
            return self._remove_node_no_childern(current_node,parent)
        if current_node.left and current_node.right:
            return self._remove_node_with_two_children(current_node)
        return self._remove_with_one_children(current_node,parent)

    def _remove_node_no_childern(self,current,parent):
        if current is self.root:
            self.root = None
            return self
        if current.value < parent.value:
            parent.left = None
        else:
            parent.right = None
        return self
    def _remove_with_one_children(self,current,parent):
        if current is self.root:
            self.root = current.right if current.right else current.left
        if parent.right == current:
            parent.right = current.right if current.right else current.left
        else:
            parent.left = current.left if current.left else current.right
        return self

    def _remove_node_with_two_children(self, current):


my_list = BinaryTree()
my_list.insert(20)
my_list.insert(16)
my_list.insert(14)
my_list.insert(13)
my_list.insert(18)
print(my_list.remove(18))
print(my_list.contains(20))
