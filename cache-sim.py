import sys

cache_size: int  # size of cache in bytes
block_size: int  # size of block in bytes
n_way: int  # associativity of the cache. 1 is direct-mapped
policy: str  # replacement policy, can be random, Fifo, or LRU
algorithm: str  # daxpy (daxpy product), mxm (matrix-matrix multiplication), or mxm_block (mxm with blocking)
matrix_dimension: int  # x by x matrix
print_mode: bool  # enables printing of the "solution" matrix product or daxpy vector after emulation
blocking_factor: int  # Use in blocked matrix multiplication algorithm


def main():
    # input flags, set at defaults
    flags = {
        '-c': 65536,
        '-b': 64,
        '-n': 1,
        '-r': 'LRU',
        '-a': 'mxm_block',
        '-d': 480,
        '-p': True,  # for now
        '-f': 32
    }

    inputs = sys.argv

    for i in range(1, len(inputs)):
        try:
            if sys.argv[i] is '-p':
                flags['-p'] = True
            else:
                flags[sys.argv[i]] = sys.argv[i + 1]  # read the flag, and the corresponding value
                i += 1  # skip over the value paired to the flag
        except IndexError:
            print("Flag indexing error occurred. Check if each flag has a corresponding value.")

    try:
        flags['-c'] = cache_size
        flags['-b'] = block_size
        flags['-n'] = n_way
        flags['-r'] = policy
        flags['-a'] = algorithm
        flags['-d'] = matrix_dimension
        flags['-p'] = print_mode
        flags['-f'] = blocking_factor
    except ValueError:
        print("Flag error occurred on value")

if __name__ == '__main__':
    main()
