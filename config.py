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

def print_configuration() -> None:
    """
    :return: prints  
    """
    print("INPUTS====================================")
    print(f"Ram Size: {cache_size} bytes")
    print(f"Cache Size: {cache_size} bytes")
    print(f"Block Size: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    print(f"Cache: {cache_size}")
    
    
