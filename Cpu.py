from Address import *
from Ram import *

import math


class Cpu:
    cache_size: int  # size of cache in bytes
    block_size: int  # size of block in bytes
    n_way: int  # associativity of the cache. 1 is direct-mapped
    policy: str  # replacement policy, can be random, Fifo, or LRU
    algorithm: str  # daxpy (daxpy product), mxm (matrix-matrix multiplication), or mxm_block (mxm with blocking)
    matrix_dimension: int  # x by x matrix
    print_mode: bool  # enables printing of the "solution" matrix product or daxpy vector after emulation
    blocking_factor: int  # Use in blocked matrix multiplication algorithm

    # computed variables from configuration inputs
    ram_size: int  # computed as the minimum memory needed to hold the daxpy or matrix-matrix multiply data structures
    set_number: int  # computed
    cached_blocks: int  # computed

    # result variables used throughout the program
    instruction_count: int
    read_hits: int
    read_misses: int
    write_hits: int
    write_misses: int

    # Ram and Cache
    ram: Ram

    def __init__(self, c=8 * 64, b=64, n=1, r='LRU', a='daxpy', d=100, p=True, f=32):
        self.cache_size = c
        self.block_size = b
        self.n_way = n
        self.policy = r
        self.algorithm = a
        self.matrix_dimension = d
        self.print_mode = p
        self.blocking_factor = f
        # computed values
        if a == 'mxm_block':
            self.ram_size = d * d * 3
        elif a == 'daxpy':
            self.ram_size = d * 3
        else:
            raise ValueError
        self.cached_blocks = int(self.cache_size / self.block_size)
        self.set_number = int(self.cached_blocks / self.n_way)
        # Initialize the Ram and Cash
        self.ram = Ram(math.ceil(self.ram_size / (self.block_size // 8)), self.block_size)
        # self.cache = Cache(int())

    def load_double(self, address):
        pass

    def store_double(self, address, value):
        adr = Address(address, self.block_size, self.set_number)
        print("Block size ", self.block_size)
        print("Address %d: block num [%d] offset [%d]" % (address, adr.block_number, adr.block_offset))
        # self.ram.set_block(adr, value)

    def add_double(self, value1, value2):
        pass

    def mult_double(self, value1, value2):
        pass

    def compute_config_variables(self):
        pass

    def print_configuration(self):
        """
        :return: prints the current configuration of the global variable inputs
        """

        print("INPUTS====================================")
        print("Ram Size = {:26d} bytes".format(self.ram_size * 8))  # computed value
        print("Cache Size = {:23d} bytes".format(self.cache_size))
        print("Block Size = {:23d} bytes".format(self.block_size))
        print("Total Blocks in cache = {:11d} blocks".format(self.cached_blocks))
        print("Associativity = {:26d}".format(self.n_way))
        print("Number of Sets = {:25d}".format(self.cache_size))
        print("Replacement Policy  = {:>20s}".format(self.policy))
        print("Algorithm  = {:>29s}".format(self.algorithm))
        print("MXM Blocking Factor  = {:19d}".format(self.blocking_factor))
        print("Matrix or Vector dimension  = {:12d}".format(self.matrix_dimension))

    def print_results(self):
        """
        :return: prints the results of the emulation
        """
        read_miss_rate = (self.read_misses / self.instruction_count) * 100  # percentage -- need to confirm
        write_miss_rate = (self.write_misses / self.instruction_count) * 100  # percentage -- need to confirm

        # to-do clean printing format this up when there's actual data -- confirm the percentages
        print("RESULTS====================================")
        print("Instruction Count = {:23d}".format(self.instruction_count))
        print("Read Hits = {:23d}".format(self.read_hits))
        print("Read Misses = {:23d}".format(self.read_misses))
        print("Read Miss Rate = {:.2f}%".format(read_miss_rate))
        print("Write Hits = {:23d}".format(self.write_hits))
        print("Write Misses = {:23d}".format(self.write_misses))
        print("Write Miss Rate = {:.2f}%".format(write_miss_rate))
