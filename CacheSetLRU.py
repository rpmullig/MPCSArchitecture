from DataBlock import *
from Address import *
from llist import dllist, dllistnode

class CacheSetLRU:

    def __init__(self, block_size: int = 64, data_value=None, n_way: int = 1):
        self.n_way = n_way
        self.data_blocks = dllist() # instead of []
        self.capacity =  n_way # associativity, capacity is number of Nones in the list
        self.tag_dictionary = dict() # Create dictionary: Key = tag, value = dllnode
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
        # Evicted block = self.data_blocks.removeleftmostnode()
        #update the dictionary:
        #remove the node in the dictionary with the key value of the EVICTED block
        #add to dictionary with new: key = address, value = dll(block)
        #self.data_blocks.appendright(block)
        pass

    def get_block(self, address):
        # get the tag from the address, and find node inside DLL from the dictionry
        # put_at_end node = self.data_blocks.remove(found_node)
        # self.data_blocks.appendright(put_at_end_node)
        # return put_at_end_node.value
        pass

    def print_data(self):
        for block in self.data_blocks:
            block.print_data()
