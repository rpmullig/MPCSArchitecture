from Address import *
from DataBlock import *


class Cache:

    def __init__(self, num_set, n_way):
        self.num_set = num_set
        self.n_way = n_way
        self.data = []
        for i in range(0, self.num_set):
            cache_set = [None] * self.n_way
            self.data.append(cache_set)

    def get_double(self, address):
        return self.data[address.get_block_number()]  # fix

    def set_double(self, address, value):
        self.get_block(address.get_index())  # fix

    def get_block(self, address):
        return self.data[address.block_number]  # fix

    def set_block(self, address, block):
        self.data[address.block_index] = block  # fix
