from __future__ import unicode_literals


class DequeNode(object):

    def __init__(self, obj, front_node, rear_node):
        self.obj = obj
        self.front_node = front_node
        self.rear_node = rear_node

    def __repr__(self):
        return "DequeNode({})".format(self.obj)

    @property
    def front_node(self):
        return self.__front_node

    @front_node.setter
    def front_node(self, new_node):
        if new_node is not None and not isinstance(new_node, DequeNode):
            raise TypeError('front_node must be DequeNode or None')
        self.__front_node = new_node

    @property
    def rear_node(self):
        return self.__rear_node

    @rear_node.setter
    def rear_node(self, new_node):
        if new_node is not None and not isinstance(new_node, DequeNode):
            raise TypeError('front_node must be DequeNode or None')
        self.__rear_node = new_node


class Deque(object):

    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.size == 0

    def _add_first_obj(self, obj):
        self.front = DequeNode(obj, None, None)
        self.rear = self.front
        self.size += 1

    def add_rear(self, obj):
        if self.size == 0:
            self._add_first_obj(obj)
        else:
            self.rear.rear_node = DequeNode(obj, self.rear, None)
            self.rear = self.rear.rear_node
            self.size += 1

    def add_front(self, obj):
        if self.size == 0:
            self._add_first_obj(obj)
        else:
            self.front.front_node = DequeNode(obj, None, self.front)
            self.front = self.front.front_node
            self.size += 1

    def _pop_last_obj(self):
        result = self.rear.obj
        self.front = self.rear = None
        self.size -= 1
        return result

    def pop_rear(self):
        if self.size == 1:
            return self._pop_last_obj()
        elif self.size == 0:
            raise Exception('is_empty')
        else:
            result = self.rear.obj
            self.rear = self.rear.front_node
            self.rear.rear_node = None
            self.size -= 1
            return result

    def pop_front(self):
        if self.size == 1:
            return self._pop_last_obj()
        elif self.size == 0:
            raise Exception('is_empty')
        else:
            result = self.front.obj
            self.front = self.front.rear_node
            self.front.front_node = None
            self.size -= 1
            return result
