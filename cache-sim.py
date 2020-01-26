import sys
import config as config


def main():
    # input flags, set at defaults
    flags = {
        '-c': 65536,
        '-b': 64,
        '-n': 1,
        '-r': 'LRU',
        '-a': 'mxm_block',
        '-d': 480,
        '-p': True,  # for now to-do make sure to add functionality to this
        '-f': 32
    }

    inputs = sys.argv
    i: int = 1  # first argument is the file name, skip that in following loop

    while i < len(inputs):
        try:
            if inputs[i] == '-p':
                flags['-p'] = True
                i += 1
            else:
                flags[inputs[i]] = inputs[i + 1]  # read the flag, and the corresponding value
                i += 2  # skip over the value paired to the flag
        except IndexError:
            print("Flag indexing error occurred. Check if each flag has a corresponding value.")
            break

    try:
        config.cache_size = int(flags['-c'])
        config.block_size = int(flags['-b'])
        config.n_way = int(flags['-n'])
        config.policy = str(flags['-r'])
        config.algorithm = str(flags['-a'])
        config.matrix_dimension = int(flags['-d'])
        config.print_mode = bool(flags['-p'])
        config.blocking_factor = int(flags['-f'])
    except ValueError:
        print("Flag error occurred on value after indexing")

    config.print_configuration()


if __name__ == '__main__':
    main()
