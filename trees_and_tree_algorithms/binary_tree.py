
class BinaryTree(object):
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, node_obj):
        if self.left_child is None:
            self.left_child = BinaryTree(node_obj)
        else:
            old_tree = self.left_child
            self.left_child = BinaryTree(node_obj)
            self.left_child.left_child = old_tree

    def insert_right(self, node_obj):
        if self.right_child is None:
            self.right_child = BinaryTree(node_obj)
        else:
            old_tree = self.right_child
            self.right_child = BinaryTree(node_obj)
            self.right_child.right_child = old_tree

    def pre_order(self):
        print self.root
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print self.root

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print self.root
        if self.right_child:
            self.right_child.in_order()


def post_order(t):
    if t.left_child:
        post_order(t.left_child)
    if t.right_child:
        post_order(t.right_child)
    print t.root


def pre_order(t):
    print t.root
    if t.left_child:
        pre_order(t.left_child)
    if t.right_child:
        pre_order(t.right_child)


def in_order(t):
    if t.left_child:
        in_order(t.left_child)
    print t.root
    if t.right_child:
        in_order(t.right_child)