from DataBlock import *
from Address import *


class Ram:

    def __init__(self, numBlocks, block_size):
        self.numBlocks = numBlocks
        self.data = []
        for i in range(numBlocks):                  # deep copy issue
            tmp = DataBlock(block_size, None)
            self.data.append(tmp)

    def print_ram(self):
        print(self.data)
        for i in range(self.numBlocks):
            print(i)
            self.data[i].print_data()
            print('-----')

    def storDouble(self, ):

    def setBlock(self, address: Address, value: DataBlock):
        pass

    def getBlock(self, address: Address):
        pass

