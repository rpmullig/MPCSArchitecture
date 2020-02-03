from Address import *
from Cache import *
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

    def __init__(self, c=65536, b=64, n=2, r='LRU', a='mxm_block', d=480, p=True, f=32):
        self.cache_size = c
        self.block_size = b
        self.n_way = n
        self.policy = r
        self.algorithm = a
        self.matrix_dimension = d
        self.print_mode = p
        self.blocking_factor = f

        self.instruction_count = 0
        self.read_hits = 0
        self.read_misses = 0
        self.write_hits = 0
        self.write_misses = 0

        # computed values determined by inputs
        if a == 'daxpy':
            self.ram_size = d * 3
        else:   # mxm_block or mxm
            self.ram_size = d * d * 3

        self.cached_blocks = int(self.cache_size / self.block_size)
        self.set_number = int(self.cached_blocks / self.n_way)
        self.ram = Ram(math.ceil(self.ram_size / (self.block_size // 8)), self.block_size)  # Initialize RAM and cache
        self.cache = Cache(self.set_number, self.n_way, self.block_size, self.policy, self)

    def load_double(self, address):
        self.instruction_count += 1
        adr = Address(address, self.block_size, self.set_number)
        return self.cache.get_double(adr)

    def store_double(self, address, value):
        self.instruction_count += 1
        adr = Address(address, self.block_size, self.set_number)
        self.ram.set_block(adr, value)
        self.cache.set_double(adr, value)

    def add_double(self, value1, value2):
        self.instruction_count += 1
        return value1 + value2

    def mult_double(self, value1, value2):
        self.instruction_count += 1
        return value1 * value2

    def print_configuration(self):
        print("INPUTS====================================")
        print("Ram Size = {:25d} bytes".format(self.ram_size * 8))  # computed value
        print("Cache Size = {:23d} bytes".format(self.cache_size))
        print("Block Size = {:23d} bytes".format(self.block_size))
        print("Total Blocks in cache = {:11d} blocks".format(self.cached_blocks))
        print("Associativity = {:26d}".format(self.n_way))
        print("Number of Sets = {:25d}".format(self.set_number))
        print("Replacement Policy  = {:>20s}".format(self.policy))
        print("Algorithm  = {:>29s}".format(self.algorithm))
        print("MXM Blocking Factor  = {:19d}".format(self.blocking_factor))
        print("Matrix or Vector dimension  = {:12d}".format(self.matrix_dimension))

    def print_results(self):
        try:
            read_miss_rate = (100.0 * self.read_misses / (self.read_misses + self.read_hits))
            write_miss_rate = (100.0 * self.write_misses / (self.write_misses + self.write_hits))

            print("RESULTS===================================")
            print("Instruction Count = {:22d}".format(self.instruction_count))
            print("Read Hits = {:30d}".format(self.read_hits))
            print("Read Misses = {:28d}".format(self.read_misses))
            print("Read Miss Rate = {:24.2f}%".format(read_miss_rate))
            print("Write Hits = {:29d}".format(self.write_hits))
            print("Write Misses = {:27d}".format(self.write_misses))
            print("Write Miss Rate = {:23.2f}%".format(write_miss_rate))
        except ValueError:
            print("Results printing error")
