
class StackNode(object):
    def __init__(self, obj, next_node):
        self.obj = obj
        assert isinstance(next_node, StackNode) or next_node is None, 'error'
        self.next_node = next_node


class Stack(object):
    def __init__(self, iterable=None):
        self.size = 0
        self.top = None
        if iterable:
            for i in iterable:
                self.push(i)

    def push(self, item):
        self.top = StackNode(item, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception('is empty.')
        pop_result = self.top.obj
        self.top = self.top.next_node
        self.size -= 1
        return pop_result

    def peek(self):
        if self.is_empty():
            raise Exception('is empty.')
        return self.top.obj

    def is_empty(self):
        return self.top is None

    def __iter__(self):
        return self

    def next(self):
        if self.size == 0:
            raise StopIteration
        else:
            return self.pop()
