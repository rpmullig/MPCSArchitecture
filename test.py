from Cpu import *
from DataBlock import *


def test():
    myCpu = Cpu(d=100)  # defaults

    sz = 8

    n = 100
    a = list(range(0, n * sz, sz))
    b = list(range(n * sz, 2 * n * sz, sz))
    c = list(range(2 * n * sz, 3 * n * sz, sz))

    test_datablock = DataBlock(64, 0)
    test_datablock.print_data()

    myCpu.ram.print_ram()
    myCpu.print_configuration()
    '''
    for i in range(n):
        myCpu.storeDouble(address=a[i], value=i)
        myCpu.storeDouble(address=b[i], value=2*i)
        myCpu.storeDouble(address=c[i], value=0)

    register0 = 3

    for i in range(n):
        register1 = myCpu.loadDouble(a[i])
        register2 = myCpu.multDouble(register0, register1)
        register3 = myCpu.loadDouble(b[i])
        register4 = myCpu.addDouble(register2, register3)
        myCpu.storeDouble(c[i], register4)
    '''


