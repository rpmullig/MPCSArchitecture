from DataBlock import *
from Address import *


class Ram:

    def __init__(self, num_blocks, block_size):
        self.numBlocks = num_blocks
        self.data = []
        for i in range(num_blocks):                  # deep copy issue
            tmp = DataBlock(block_size, None)
            self.data.append(tmp)

    def print_ram(self):
        print(self.data)
        for i in range(self.numBlocks):
            print(i)
            self.data[i].print_data()
            print('-----')

    def set_block(self, address, value):
        self.data[address.get_block_number()].set_value(address.get_offset(), value)

    def get_block(self, address):
        return self.data[address.get_block_number()]

