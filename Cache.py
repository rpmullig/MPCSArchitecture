from CacheSetRandom import *
from CacheSetLRU import *
from Address import *
from random import *


class Cache:

    def __init__(self, num_set, n_way: int, block_size: int, policy: str = "LRU", cpu=object):
        self.num_set = num_set
        self.n_way = n_way
        self.policy = policy
        self.cache_sets = []
        self.cpu = cpu
        for i in range(0, self.num_set):  # CacheSet is a "row" in the cache - size, data, associativity
            if self.policy == "random":
                self.cache_set = CacheSetRandom(block_size, None, n_way)
            elif self.policy == "LRU":
                self.cache_set = CacheSetLRU(block_size, None, n_way)
            else:
                print("FIFO not installed")
            self.cache_sets.append(self.cache_set)

    def get_double(self, address: Address):
        retrieved_set = self.cache_sets[address.get_index()]
        this_tag = address.get_tag()

        # Check if block exists
        if self.policy != "LRU":
            for i in range(0, retrieved_set.n_way):
                # possible error in None value, so make sure that's not the case
                if retrieved_set.tags[i] == this_tag and retrieved_set.data_blocks[i] is not None:
                    self.cpu.read_hits += 1
                    return retrieved_set.data_blocks[i].get_value(address.get_offset())
        else:  # LRU
            if this_tag in retrieved_set.tag_dictionary:
                this_node = retrieved_set.tag_dictionary[this_tag]
                index = 0
                for i in range(retrieved_set.data_blocks.size):
                    current_node = retrieved_set.data_blocks.nodeat(i)
                    if current_node.value[1] is this_tag:
                        self.cpu.read_hits += 1
                        index = i
                        # swap to front of the list
                        touched_node = retrieved_set.data_blocks.nodeat(index)
                        retrieved_set.data_blocks.remove(touched_node)
                        retrieved_set.data_blocks.appendright(touched_node)
                        touched_block = touched_node.value[0]
                        return touched_block.get_value(address.get_offset())  # returns a block

                # Get block from RAM
                self.cpu.read_misses += 1
                ram_block = self.cpu.ram.get_block(address)
                self.set_block_with_replacement(address, ram_block)
                return ram_block.get_value(address.get_offset())

            else:
                # Get block from RAM
                self.cpu.read_misses += 1
                ram_block = self.cpu.ram.get_block(address)
                self.set_block_with_replacement(address, ram_block)
                return ram_block.get_value(address.get_offset())

        # Get block from RAM
        self.cpu.read_misses += 1
        ram_block = self.cpu.ram.get_block(address)
        self.set_block_with_replacement(address, ram_block)
        return ram_block.get_value(address.get_offset())

    def set_double(self, address: Address, value):
        retrieved_set = self.cache_sets[address.get_index()]
        none_position = -1
        if_block_exists = False

        if self.policy == "LRU":

            if address.get_tag() in retrieved_set.tag_dictionary:
                if retrieved_set.tag_dictionary[address.get_tag()].value[0].get_value(address.get_offset()) == value:
                    if_block_exists = True
                    self.cpu.write_hits += 1
                    return

            if if_block_exists is not True:
                # Get block from RAM
                self.cpu.write_misses += 1
                ram_block = self.cpu.ram.get_block(address)

                # None position = capacity, still filling the set ---- Compulsary
                if retrieved_set.capacity > 0:

                    retrieved_set.capacity -= 1
                    tag = address.get_tag()
                    block_node = dllistnode([ram_block, tag])
                    retrieved_set.data_blocks.appendright(block_node)
                    # retrieved_set.tag_dictionary[tag] = block_node

                    location = len(retrieved_set.data_blocks) - 1  # new location of the node
                    retrieved_set.tag_dictionary[tag] = retrieved_set.data_blocks.nodeat(location)
                    # Need to add key:tag, value: retrieved_set.getrightnode()
                else:
                    self.set_block_with_replacement(address, ram_block)
        else:

            # Search for None Blocks in the set :
            none_position = retrieved_set.search_for_none(address)

            # Random and FIFO Policies
            for i in range(0, retrieved_set.n_way):
                this_tag = address.get_tag()
                if retrieved_set.tags[i] == this_tag:
                    if retrieved_set.data_blocks[i].get_value(address.get_offset()) == value:
                        self.cpu.write_hits += 1
                        if_block_exists = True
                        return
                    # else:
                    # retrieved_set.data_blocks[i].set_value(address.get_offset(), value)

            if if_block_exists is False:
                # Get block from RAM
                self.cpu.write_misses += 1

                ram_block = self.cpu.ram.get_block(address)

                if none_position < 0:  # If there doesnt exist a none block
                    # Cache full, need to use replacement policy
                    self.set_block_with_replacement(address, ram_block)
                else:
                    if self.policy != "LRU":  # not needed, but just to be sure
                        # Need to set block into None position
                        retrieved_set.tags[none_position] = address.get_tag()
                        retrieved_set.data_blocks[none_position] = ram_block

    def set_block_with_replacement(self, address, block):

        current_set = self.cache_sets[address.get_index()]
        i: int = 0
        if self.policy == "random":
            i = randrange(0, self.n_way)  # Random from 0 to n_associativity
            self.cache_sets[address.get_index()].tags[i] = address.get_tag()
            self.cache_sets[address.get_index()].data_blocks[i] = block
        elif self.policy == "LRU":
            remove_node = current_set.data_blocks.pop()
            remove_tag = remove_node[1]

            del current_set.tag_dictionary[remove_tag]

            add_tag = address.get_tag()
            add_node = dllistnode([block, add_tag])
            current_set.data_blocks.appendright(add_node)
            # current_set.tag_dictionary[add_tag] = add_node
            current_set.tag_dictionary[add_tag] = current_set.data_blocks.nodeat(len(current_set.data_blocks) - 1)

        else:  # must be FIFO
            pass
            # i = current_set.first_in

    def print_cache(self):
        # print(self.cache_sets)
        print("---------CACHE DATA---------")
        for i in range(self.num_set):
            print("set: %d" % i)
            self.cache_sets[i].print_data()
            print('-----')
