import sys
from Cpu import *
from test import *


def main() -> None:
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

    c = int(flags['-c'])
    b = int(flags['-b'])
    n = int(flags['-n'])
    r = str(flags['-r'])
    a = str(flags['-a'])
    d = int(flags['-d'])
    p = bool(flags['-p'])
    f = int(flags['-f'])

    test()

    # cpu = Cpu(c, b, n, r, a, d, p, f)
    # cpu.print_configuration()


if __name__ == '__main__':
    main()
