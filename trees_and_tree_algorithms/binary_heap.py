
class BinaryMinHeap(object):

    def __init__(self, l=None):
        self.heap_list = [0]
        self.size = 0
        if l:
            self.size = len(l)
            i = self.size // 2
            self.heap_list = self.heap_list + l
            while i > 0:
                self.perc_down(i)
                i -= 1

    def get_min(self):
        return self.heap_list[1]

    def del_min(self):
        result = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return result

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def get_min_child_index(self, index):
        if index * 2 > self.size:
            return None
        elif index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2 + 1
            else:
                return index * 2

    def perc_down(self, index):
        while index * 2 < self.size:
            min_child_index = self.get_min_child_index(index)
            if self.heap_list[index] > self.heap_list[min_child_index]:
                self.heap_list[min_child_index], self.heap_list[index] = self.heap_list[index], self.heap_list[min_child_index]
            index = min_child_index

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]
            index = index // 2

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.perc_up(self.size)
