from CacheSet import *
from Address import *


class Cache:

    def __init__(self, num_set, n_way: int, block_size: int, policy="LRU"): #add cpu
        #add self.cpu = cpu
        self.num_set = num_set
        self.n_way = n_way
        self.policy = policy
        self.cache_sets = []
        for i in range(0, self.num_set):
            cache_set = CacheSet(False, None, block_size, None, n_way)  # A "row" in the cache - Valid bit, tag, data
            self.cache_sets.append(cache_set)

    def get_double(self, address: Address):
        index = address.get_index()
        tag = address.get_tag()
        retrieved_set = self.cache_sets[index]

        '''

        if_block_exists = False

        
        for block in retrieved_set:
            if block.get_tag() == address.tag():
                self.cpu.read_hit += 1
                return block.getValue(address.getOffset())
        
        if (if_block_exists == False):
            self.cpu.read_miss += 1
            
            #GET THE BLOCK FROM RAM 
            ram_block = self.cpu.ram.getBlock(index)
            
            setReplacementPolicy(addr, ram_block)
            
            return ram_block.getValue(addr.offset())

        '''



    def set_double(self, address: Address, value):
        index = address.get_index()
        tag = address.get_tag()

        retrieved_set = self.cache_sets[index]

        '''
        NEED TO FIGURE OUT IF THERE ARE NONE BLOCKS EXISTING IN THE SET:
        
        none_position = -1
        if_block_exists = False
        
        for i in len(retrieved_set):
            if(retrieved_set[i] == None):
                none_position = i
                break
        
        for block in retrieved_set:
            if block.get_tag() == address.tag():
                self.cpu.hit += 1
                block.setValue(address.getOffset(), value)
                if_block_exists = True
                break
        
        
        if (if_block_exists == False):
            self.cpu.write_miss += 1
            
            #GET THE BLOCK FROM RAM 
            ram_block = self.cpu.ram.getBlock(index)
            if(none_position = -1): #IF there doesnt exist a none block
                #FULL, need to use replacement policy
                self.setBlockWithReplacement(ram_block)
            else:
                #NEED TO SET BLOCK INTO NONE POSITION
                retrieved_set[none_position] = ram_block

        
                
                
        '''

        '''
        for current_set in self.cache_sets:
            if current_set.get_validation_bit() is False:
                current_set.set_validation_bit(True)
                current_set.set_block(address, value)
        '''

    def setBlockWithReplacment(self, address, block):
        #Random from 0 to n_associativity
        #Set cache_sets[address.index][random(0, n_way)] = block




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
'''