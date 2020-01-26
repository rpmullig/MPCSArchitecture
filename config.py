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

# computed variables
ram_size: int  # computed as the minimum memory needed to hold the daxpy or matrix-matrix multiply data structures


# result variables


def compute_variables() -> None:
    pass


def print_configuration() -> None:
    """
    :return: prints the current configuration of the global variable inputs
    """
    compute_variables()  # compute variables from the ones that were passed

    print("INPUTS====================================")
    # print("Ram Size = {:26d} bytes".format(ram_size))  # computed value
    print("Cache Size = {:26d} bytes".format(cache_size))
    print("Block Size = {:26d} bytes".format(cache_size))
    print("Total Blocks in cache = {:26d} bytes".format(cache_size))
    print("Associativity = {:26d} bytes".format(cache_size))
    print("Number of Sets: {:26d} bytes".format(cache_size))
    print("Replacement Policy: {:26d} bytes".format(policy))
    print("Number of Sets: {:26d} bytes".format(cache_size))
    print("Number of Sets: {:26d} bytes".format(cache_size))


def print_results() -> None:
    pass
