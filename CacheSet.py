from DataBlock import *
from Address import *


class CacheSet:

    def __init__(self, block_size: int = 64, data_value=None, n_way: int = 1):
        self.n_way = n_way
        self.data_blocks = []
        self.tags = [None] * n_way
        self.last_used_block = [None, 0]  # DataBlock and block number
        self.first_in = None
        for i in range(0, n_way):
            tmp = DataBlock(block_size, data_value)
            self.data_blocks.append(tmp)

    def search_for_none(self, address: Address):
        for i in range(0, self.n_way):
            if self.data_blocks[i].get_value(address.get_offset()):
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

    def set_block(self, address, value):
        self.data_blocks[address.get_block_number()].set_value(address.get_offset(), value)
        self.first_in = address.get_offset()

    def get_block(self, address):
        self.last_used_block = self.data_blocks[address.get_block_number()]
        return self.data_blocks[address.get_block_number()]

    def get_last_recently_used(self):
        return self.last_used_block

    def print_data(self):
        for block in self.data_blocks:
            block.print_data()
