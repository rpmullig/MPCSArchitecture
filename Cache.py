from CacheSet import *
from Address import *


class Cache:

    def __init__(self, num_set, n_way: int, block_size: int, policy="LRU"):
        self.num_set = num_set
        self.n_way = n_way
        self.policy = policy
        self.cache_sets = []
        for i in range(0, self.num_set):
            cache_set = CacheSet(False, None, block_size, None, n_way)  # A "row" in the cache - Valid bit, tag, data]
            self.cache_sets.append(cache_set)

    def get_double(self, address: Address):
        index = address.get_index()
        tag = address.get_tag()
        for cache_set in range(self.num_set):
            current_set: CacheSet() = self.cache_sets[index]
            if current_set.get_cache_set_tag() == tag and current_set.get_validation_bit() is True:
                return current_set.get_block(address).get_value()
        else:
            return False

    def set_double(self, address: Address, value):
        index = address.get_index()
        tag = address.get_tag()
        for current_set in self.cache_sets:
            if current_set.get_validation_bit() is False:
                current_set.set_validation_bit(True)
                current_set.set_block(address, value)

    def print_cache(self):
        # print(self.cache_sets)
        print("---------CACHE DATA---------")
        for i in range(self.num_set):
            print("set: %d" % i)
            self.cache_sets[i].print_data()
            print('-----')


'''

    set_dict = dict()
            for x in range(0, self.n_way):
                set_dict[i] = [False, None]  # valid bit and tag per each data block



    def get_double(self, address):
        tag = address.block_tag
        index = address.block_index
        target_set = self.data[index]
        target_set_meta_data = self.meta_data_on_set[index]
        for b in range(0, len(target_set)):
            if target_set_meta_data[b][1] == tag and target_set_meta_data[b][0] is True:
                return [True, target_set[b]]  # hit status and data
        return [False, 0]

    def set_double_least_recently_used(self, address, value):
        if self.at_capacity is False:
            self.get_block(address.get_index())

    def set_double_first_in_first_out(self, address, value):
        if self.at_capacity is False:
            self.get_block(address.get_index())

    def set_double_random(self, address, value):
        if self.at_capacity is False:
            self.get_block(address.get_index())

    def get_block(self, address):
        return self.data[address.block_number]

    def set_block(self, address, block):
        self.data[address.block_index] = block
'''
