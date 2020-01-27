from Address import *
from DataBlock import *


class Cache:

    def __init__(self, num_set, num_blocks):
        self.numSet = num_set
        self.numBlocks = num_blocks
        self.blocks = [DataBlock(num_set) for x in range(0, num_blocks)]

    def get_double(self, address: Address):
        pass

    def set_double(self, address: Address, value: float):
        pass

    def get_block(self, address: Address):
        pass

    def set_block(self, address: Address, block: DataBlock):
        pass
