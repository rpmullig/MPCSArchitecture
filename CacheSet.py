from DataBlock import *


class CacheSet:

    def __init__(self, validation_bit=False, tag=None, block_size: int = 64, data_value=None, n_way: int = 1):
        self.validation_bit = validation_bit
        self.tag = tag
        self.data_blocks = []
        for i in range(0, n_way):
            tmp = DataBlock(block_size, data_value)
            self.data_blocks.append(tmp)

    def get_cache_set_tag(self):
        return self.tag

    def compare_cache_set_tag(self, tag):
        return self.tag == tag

    def get_validation_bit(self):
        return self.validation_bit

    def set_validation_bit(self, new_bit):
        self.validation_bit = new_bit

    def set_block(self, address, value):
        self.data_blocks[address.get_block_number()].set_value(address.get_offset(), value)

    def get_block(self, address):
        return self.data_blocks[address.get_block_number()]

    def get_last_recently_used(self):
        """
        Gets the last recently use block in the set
        :return: 
        """""
        tmp_oldest = self.data_blocks[0].get_last_update_time()
        for block in self.data_blocks:
            tmp_time = block.get_last_update_time()
            if tmp_oldest > tmp_time:
                tmp_oldest = tmp_time  # update the oldest value
        return tmp_oldest

    def print_data(self):
        for block in self.data_blocks:
            block.print_data()