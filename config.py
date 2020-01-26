"""
Global variables for us in the file
"""
# emulator inputs as configuration variables
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

#  computed variables from emulation results



def compute_config_variables() -> None:
    pass


def print_configuration() -> None:
    """
    :return: prints the current configuration of the global variable inputs
    """
    compute_config_variables()  # compute variables from the ones that were passed

    print("INPUTS====================================")
    # print("Ram Size = {:26d} bytes".format(ram_size))  # computed value
    print("Cache Size = {:23d} bytes".format(cache_size))
    print("Block Size = {:23d} bytes".format(block_size))
    # print("Total Blocks in cache = {:26d} bytes".format(cached_blocks))
    print("Associativity = {:26d}".format(n_way))
    print("Number of Sets = {:25d}".format(cache_size))
    print("Replacement Policy  = {:>20s}".format(policy))
    print("Algorithm  = {:>29s}".format(algorithm))
    print("MXM Blocking Factor  = {:19d}".format(blocking_factor))
    print("Matrix or Vector dimension  = {:12d}".format(matrix_dimension))


def compute_result_variables():
    pass


def print_results() -> None:
    """
    :return: prints the results of the emulation
    """
    compute_result_variables()

    print("RESULTS====================================")
    pass
