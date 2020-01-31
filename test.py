from Cpu import *


def test():
    my_cpu = Cpu(d=100)  # defaults

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

    my_cpu.ram.print_ram()
    my_cpu.cache.print_cache()

    register0 = 3
    '''
    # my_cpu.print_configuration()
    # print(test_addr)

    for i in range(n):
        register1 = my_cpu.loadDouble(a[i])
        register2 = my_cpu.multDouble(register0, register1)
        register3 = my_cpu.loadDouble(b[i])
        register4 = my_cpu.addDouble(register2, register3)
        my_cpu.storeDouble(c[i], register4)
    '''
