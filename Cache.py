from CacheSet import *
from Address import *
from random import *


class Cache:

    def __init__(self, num_set, n_way: int, block_size: int, policy: str = "LRU", cpu=object):
        self.num_set = num_set
        self.n_way = n_way
        self.policy = policy
        self.cache_sets = []
        self.cpu = cpu
        for i in range(0, self.num_set):
            cache_set = CacheSet(block_size, None, n_way)  # A "row" in the cache - size, data, associativity
            self.cache_sets.append(cache_set)

    def get_double(self, address: Address):
        retrieved_set: CacheSet = self.cache_sets[address.get_index()]
        this_tag = address.get_tag()

        # Check if block exists
        for i in range(0, retrieved_set.n_way):
            # possible error in None value, so make sure that's not the case
            if retrieved_set.tags[i] is this_tag and retrieved_set.data_blocks[i].get_value(
                    address.get_offset()) is not None:
                self.cpu.read_hits += 1
                return retrieved_set.data_blocks[i].get_value(address.get_offset())

        # Get block from RAM
        self.cpu.read_misses += 1
        ram_block = self.cpu.ram.get_block(address)
        self.set_block_with_replacement(address, ram_block)

        return ram_block.get_value(address.get_offset())

    def set_double(self, address: Address, value):
        retrieved_set: CacheSet = self.cache_sets[address.get_index()]
        none_position = -1
        if_block_exists = False

        # Search for None Blocks in the set :
        none_position = retrieved_set.search_for_none(address)  # not ideal / clean

        for i in range(0, retrieved_set.n_way):
            this_tag = address.get_tag()
            if retrieved_set.tags[i] == this_tag:
                self.cpu.write_hits += 1
                retrieved_set.data_blocks[i].set_value(address.get_offset(), value)
                if_block_exists = True
                break

        if not if_block_exists:
            self.cpu.write_misses += 1

            # Get block from RAM
            ram_block = self.cpu.ram.get_block(address)
            if none_position < 0:  # If there doesnt exist a none block
                # Cache full, need to use replacement policy
                self.set_block_with_replacement(address, ram_block)
            else:
                # Need to set block into None position
                self.cache_sets[address.get_index()].tags[none_position] = address.get_tag()
                ram_block_value = ram_block.get_value(address.get_offset())
                self.cache_sets[address.get_index()].data_blocks[none_position].set_value(address.get_offset(),
                                                                                          ram_block_value)

    def set_block_with_replacement(self, address, block):
        ram_block_value = block.get_value(address.get_offset())
        current_set = self.cache_sets[address.get_index()]
        i: int = 0
        if self.policy is "random":
            # Random from 0 to n_associativity
            i = randrange(0, self.n_way)
        elif self.policy is "LRU":
            pass
            # i = current_set.first_in
        else:  # must be FIFO
            pass
            # i = current_set.first_in

        address.set_offset(i)
        self.cache_sets[address.get_index()].tags[i] = address.get_tag()
        self.cache_sets[address.get_index()].data_blocks[i].set_value(address.get_offset(), ram_block_value)
        # self.cache_sets[i].set_value(address, ram_block_value)
        # elif self.policy is "LRU":
        #    for set in self.cache_sets:

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

                # self.cache_sets[none_position].set_block(address, ram_block.get_value(address.get_offset()))

-------
for current_set in self.cache_sets:
    if current_set.get_validation_bit() is False:
        current_set.set_validation_bit(True)
        current_set.set_block(address, value)
'''
