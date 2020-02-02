from DataBlock import *
from Address import *
from llist import *


class CacheSetLRU:

    def __init__(self, block_size: int = 64, data_value=None, n_way: int = 1):
        self.n_way = n_way
        self.data_blocks = dllist()  # instead of []
        self.capacity = n_way  # associativity, capacity is number of Nones in the list
        self.tag_dictionary = dict()  # Create dictionary: Key = tag, value = dllnode
        self.tags = [None] * n_way
        self.first_in = None

    def get_blocks(self):
        return self.data_blocks

    def get_tags(self):
        return self.tags

    def get_tag(self, address):
        return self.tags[address.get_block_number()]

    def set_tag(self, address):
        self.tags[address.get_block_number()] = address.get_tag()

    def print_data(self):
        for block in self.data_blocks:
            block.print_data()
