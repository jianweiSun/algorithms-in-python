
class HashTable(object):

    def __init__(self, slots_num):
        self.slots_num = slots_num
        self.slots = [None] * slots_num
        self.datas = [None] * slots_num

    def hash_func(self, key):
        assert isinstance(key, int), u'Could only be integer.'
        slot_index = key % self.slots_num
        return slot_index

    def rehash(self, orig_hash_value):
        return (orig_hash_value+1) % self.slots_num

    def put(self, key, value):
        hash_value = self.hash_func(key)
        orig_hash_value = hash_value

        while self.slots[hash_value] is not None and self.slots[hash_value] != key:
            hash_value = self.rehash(hash_value)
            if hash_value == orig_hash_value:
                raise Exception('slots is full.')

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.datas[hash_value] = value
        else:
            self.datas[hash_value] = value

    def get(self, key):
        hash_value = self.hash_func(key)
        orig_hash_value = hash_value

        while self.slots[hash_value] != key:
            hash_value = self.rehash(hash_value)
            if hash_value == orig_hash_value:
                raise Exception('key not found.') # not found

        return self.datas[hash_value]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)
