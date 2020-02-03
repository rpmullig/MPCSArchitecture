import sys
from Cpu import *


def main() -> None:
    # input flags, set at defaults
    flags = {
        '-c': 65536,
        '-b': 64,
        '-n': 2,
        '-r': 'LRU',
        '-a': 'mxm_block',
        '-d': 480,
        '-p': False,
        '-f': 32
    }

    inputs = sys.argv
    i = 1  # first argument is the file name, skip that in following loop

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

    # test()

    my_cpu = Cpu(c, b, n, r, a, d, p, f)
    # cpu.print_configuration()
    n = my_cpu.matrix_dimension

    if my_cpu.algorithm == "daxpy":

        sz = 1

        a = list(range(0, n * sz, sz))
        b = list(range(n * sz, 2 * n * sz, sz))
        c = list(range(2 * n * sz, 3 * n * sz, sz))

        for i in range(n):
            my_cpu.store_double(address=a[i], value=i)
            my_cpu.store_double(address=b[i], value=2 * i)
            my_cpu.store_double(address=c[i], value=0)

        register0 = 3

        for i in range(n):
            register1 = my_cpu.load_double(a[i])
            register2 = my_cpu.mult_double(register0, register1)
            register3 = my_cpu.load_double(b[i])
            register4 = my_cpu.add_double(register2, register3)
            my_cpu.store_double(c[i], register4)

    elif my_cpu.algorithm == "mxm_block":

        a = list(range(0, n * n, 1))
        b = list(range(n * n, 2 * n * n, 1))
        c = list(range(2 * n * n, 3 * n * n, 1))

        for i in range(n * n):
            my_cpu.store_double(address=a[i], value=i)
            my_cpu.store_double(address=b[i], value=2 * i)
            my_cpu.store_double(address=c[i], value=0)

        blocking_factor = my_cpu.blocking_factor

        for kk in range(0, n, blocking_factor):
            for jj in range(0, n, blocking_factor):
                for i in range(n):
                    for j in range(jj, jj + blocking_factor):
                        register0 = my_cpu.load_double(address=c[i * n + j])
                        # sum = c[i][j]
                        for k in range(kk, kk + blocking_factor):
                            register1 = my_cpu.load_double(address=a[i * n + k])
                            register2 = my_cpu.load_double(address=b[k * n + j])
                            register3 = my_cpu.mult_double(register1, register2)
                            register0 = my_cpu.add_double(register0, register3)
                            # sum += a[i][k] * b[k][j]

                        my_cpu.store_double(address=c[i * n + j], value=register0)

    elif my_cpu.algorithm == "mxm":

        a = list(range(0, n * n, 1))
        b = list(range(n * n, 2 * n * n, 1))
        c = list(range(2 * n * n, 3 * n * n, 1))

        for i in range(n * n):
            my_cpu.store_double(address=a[i], value=i)
            my_cpu.store_double(address=b[i], value=2 * i)
            my_cpu.store_double(address=c[i], value=0)

        for i in range(n):
            for j in range(n):
                register0 = 0
                for k in range(n):
                    register1 = my_cpu.load_double(address=a[i * n + k])
                    register2 = my_cpu.load_double(address=b[k * n + j])
                    register3 = my_cpu.mult_double(register1, register2)
                    register0 = my_cpu.add_double(register0, register3)
                my_cpu.store_double(c[i * n + j], register0)

    # my_cpu.cache.print_cache()
    my_cpu.print_configuration()
    my_cpu.print_results()

    if my_cpu.print_results is True:
        result_matrix = []
        for address in c:
            result_matrix.append(my_cpu.load_double(address=address))

        print("\n\nResulting Matrix:\n")
        print(result_matrix)


if __name__ == '__main__':
    main()
