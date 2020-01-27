from Address import *
from DataBlock import *


class Cache:

    def __init__(self, num_set, n_way):
        self.num_set = num_set
        self.n_way = n_way
        self.data = []
        for i in range(0, self.num_set):
            set = [[0, None] * self.n_way]  # validation bit and value
            self.data.append(set)

    def get_double(self, address):
        return self.data[address.get_block_number()]

    def set_double(self, address, value):
        pass
        # self.data[address.get_block_number()].set_value(address.get_offset(), value)

    def get_block(self, address):
        pass
        # self.data[cpu.ram.get_block(address)]  # wrong

    def set_block(self, address, block):
        pass
        # self.data[.set_block(address, block)  # wrong
