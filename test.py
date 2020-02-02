from Cpu import *


def test():
    my_cpu = Cpu(n=4, d=100, r="LRU")  # defaults

    sz = 1

    n = 10000
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

    # my_cpu.ram.print_ram()
    my_cpu.cache.print_cache()
    my_cpu.print_configuration()
    my_cpu.print_results()

