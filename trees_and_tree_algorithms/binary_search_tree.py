
class BinarySearchTree(object):

    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left:
                self._put(key, value, current_node.left)
            else:
                current_node.left = TreeNode(key, value, parent=current_node)
        else:
            if current_node.right:
                self._put(key, value, current_node.right)
            else:
                current_node.right = TreeNode(key, value, parent=current_node)

    def get(self, key):
        if self.root:
            match_node = self._get(key, self.root)
            if match_node:
                return match_node.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self.get(key)
            if node_to_delete:
                self.remove(node_to_delete)
                self.size -= 1
            else:
                raise KeyError("Error, Key not found.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, Key not found.")

    def remove(self, node):
        assert isinstance(node, TreeNode)
        if node.is_leaf():
            if node is node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_both_child():
            successor = node.find_successor()
            successor.spice_out()
            node.key = successor.key
            node.value = successor.value
        else:  # has only one child
            if node.left:
                if node.is_left_child():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.is_right_child():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.replace_node_data(node.left.key,
                                           node.left.value,
                                           node.left.left,
                                           node.left.right)
            else:
                if node.is_left_child():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.is_right_child():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replace_node_data(node.right.key,
                                           node.right.value,
                                           node.right.left,
                                           node.right.right)


class TreeNode(object):

    def __init__(self, key, value, left=None, right=None, parent=None):

        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not (self.left or self.right)

    def has_any_child(self):
        return self.left or self.right

    def has_both_child(self):
        return self.left and self.right

    def replace_node_data(self, key, value, left, right):

        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def find_successor(self):
        succ = None
        if self.right:
            succ = self.right.find_min()  # BinarySearchTree delete will always has self.right
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.find_successor()
                    self.parent.right = self
        return succ

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def spice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_child():
            if self.left:
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def __iter__(self):
        if self:
            if self.left:
                for elem in self.left:
                    yield elem
            yield self.key
            if self.right:
                for elem in self.right:
                    yield elem
