from __future__ import unicode_literals


class ListNode(object):
    def __init__(self, obj, prev_node, next_node):
        self.obj = obj
        self.next_node = next_node
        self.prev_node = prev_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and not isinstance(next_node, ListNode):
            raise Exception('Must be ListNode or None.')
        self.__next_node = next_node

    @property
    def prev_node(self):
        return self.__prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        if prev_node is not None and not isinstance(prev_node, ListNode):
            raise Exception('Must be ListNode or None.')
        self.__prev_node = prev_node


class List(object):

    def __init__(self, iterable=None):
        if not iterable:
            self.size = 0
            self.last = None
            self.front = None

    def __len__(self):
        return self.size

    def __repr__(self):
        result = ''
        for obj in self:
            result += ' ' + str(obj)
        return result

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                index = index + len(self)
            return getattr(self, str(index)).obj
        elif isinstance(index, slice):
            start = index.start if index.start else 0
            stop = index.stop if index.stop else len(self)
            new_list = List()
            current_node = self.front
            for i in range(stop):
                if i >= start:
                    new_list.append(current_node.obj)
                current_node = current_node.next_node
            return new_list

    def __setitem__(self, index, item):
        node = getattr(self, str(index))
        node.obj = item

    def __iter__(self):
        current_node = self.front
        for i in range(len(self)):
            yield current_node.obj
            current_node = current_node.next_node

    def append(self, obj):
        if len(self) == 0:
            self.last = self.front = ListNode(obj, None, None)
        else:
            self.last.next_node = ListNode(obj, self.last, None)
            self.last = self.last.next_node

        setattr(self, str(len(self)), self.last)
        self.size += 1

    def search(self, search_item):
        for obj in self:
            if obj == search_item:
                return True
        return False

    def remove(self, remove_item):
        current_node = self.front
        if self.size == 1:
            self.__init__()
            delattr(self, '0')
        else:
            item_is_removed = False
            for i in range(len(self)):
                if item_is_removed:
                    setattr(self, str(i - 1), current_node)
                else:
                    if current_node.obj == remove_item:
                        if i == 0:
                            current_node.next_node.prev_node = None
                            self.front = current_node.next_node
                        elif i == len(self) - 1:
                            current_node.prev_node.next_node = None
                            self.last = current_node.prev_node
                        else:
                            current_node.prev_node.next_node = current_node.next_node
                            current_node.next_node.prev_node = current_node.prev_node
                        self.size -= 1
                        item_is_removed = True

                    current_node = current_node.next_node

            if item_is_removed:
                delattr(self, str(self.size))
            else:
                raise ValueError('{} not in list.'.format(remove_item))

    def pop(self, index=None):
        if not index:
            index = len(self) - 1

        if self.size == 1:
            result = self.front.obj
            self.__init__()
            delattr(self, '0')
        else:
            node = getattr(self, str(index))
            result = node.obj
            if index == 0:
                node.next_node.prev_node = None
                self.front = node.next_node
            elif index == len(self) - 1:
                node.prev_node.next_node = None
                self.last = node.prev_node
            else:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
            self.size -= 1

            for i in range(index + 1, self.size):
                setattr(self, str(i - 1), getattr(self, str(i)))

            delattr(self, str(self.size))

        return result

    def insert(self, index, item):
        if index >= len(self):
            self.append(item)
        else:
            if index == 0:
                new_node = ListNode(item, None, self.front)
                self.front.prev_node = new_node
                self.front = new_node
            else:
                insert_prev_node = getattr(self, str(index-1))
                insert_after_node = getattr(self, str(index))
                new_node = ListNode(item, insert_prev_node, insert_after_node)
                insert_prev_node.next_node = new_node
                insert_after_node.prev_node = new_node

            for i in range(self.size - 1, index - 1, -1):
                setattr(self, str(i + 1), getattr(self, str(i)))

            self.size += 1
            setattr(self, str(index), new_node)

