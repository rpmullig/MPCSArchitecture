from DataBlock import *
from Address import *


class CacheSetRandom:

    def __init__(self, block_size: int = 64, data_value=None, n_way: int = 1):
        self.n_way = n_way
        self.data_blocks = []
        self.tags = [None] * n_way
        self.first_in = None
        for i in range(0, n_way):
            tmp = DataBlock(block_size, data_value)
            self.data_blocks.append(tmp)

    def search_for_none(self, address: Address):
        for i in range(0, self.n_way):
            if self.data_blocks[i] is None:
                return i
        return -1

    def get_blocks(self):
        return self.data_blocks

    def get_tags(self):
        return self.tags

    def get_tag(self, address):
        return self.tags[address.get_block_number()]

    def set_tag(self, address):
        self.tags[address.get_block_number()] = address.get_tag()

    def set_block(self, address, block):
        self.data_blocks[address.get_block_number()] = block

    def get_block(self, address):
        return self.data_blocks[address.get_block_number()]

    def print_data(self):
        for block in self.data_blocks:
            block.print_data()
