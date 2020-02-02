from Cpu import *


def test():
    my_cpu = Cpu()  # defaults

    if my_cpu.algorithm == "daxpy":
        sz = 1

        n = 100
        a = list(range(0, n * sz, sz))
        b = list(range(n * sz, 2 * n * sz, sz))
        c = list(range(2 * n * sz, 3 * n * sz, sz))

        # test_datablock = DataBlock(64, 0)
        # test_datablock.print_data()

        # test_addr = Address(3, 64, 8)
        for i in range(n):
            my_cpu.store_double(address=a[i], value=i)
            my_cpu.store_double(address=b[i], value=2 * i)
            my_cpu.store_double(address=c[i], value=0)

        register0 = 3

        # my_cpu.print_configuration()
        # print(test_addr)

        for i in range(n):
            register1 = my_cpu.load_double(a[i])
            register2 = my_cpu.mult_double(register0, register1)
            register3 = my_cpu.load_double(b[i])
            register4 = my_cpu.add_double(register2, register3)
            my_cpu.store_double(c[i], register4)

    elif my_cpu.algorithm == "mxm_block":

        n = my_cpu.n_way
        a = list(range(0, n * n, 1))
        b = list(range(n * n, 2 * n * n, 1))
        c = list(range(2 * n * n, 3 * n * n, 1))

        tmp = 0
        for i in range(n*n):
            my_cpu.store_double(address=a[i], value=i)
            my_cpu.store_double(address=b[i], value=2*i)
            my_cpu.store_double(address=c[i], value=0)

        for i in range(0, n, my_cpu.blocking_factor): 
            for j in range(0, n, my_cpu.blocking_factor):
                for x in range(n): 
                    for z in range(j, j + my_cpu.blocking_factor):
                        register0 = my_cpu.load_double(address=(n*n + x))
                        for y in range(i, i + my_cpu.blocking_factor): 
                            register1 = my_cpu.load_double()

    my_cpu.cache.print_cache()
    my_cpu.print_configuration()
    my_cpu.print_results()
