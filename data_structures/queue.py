
class QueueNode(object):

    def __init__(self, obj, next_node):
        self.obj = obj
        self.next_node = next_node


class Queue(object):

    def __init__(self, iterable=None):
        self.size = 0
        self.front = None
        self.last = None

    def enqueue(self, item):
        if self.size == 0:
            self.front = QueueNode(item, None)
            self.last = self.front
        else:
            self.last.next_node = QueueNode(item, None)
            self.last = self.last.next_node

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("is empty")
        result = self.front.obj
        self.front = self.front.next_node
        return result

    def is_empty(self):
        return self.size == 0
