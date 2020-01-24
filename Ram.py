import DataBlock as DataBlock
import Address as Address


class Ram:
    numBlocks: int
    data: DataBlock

    def __init__(self, numBlocks, data):
        self.numBlocks = numBlocks
        self.data = data

    def setBlock(self, address: Address, value: DataBlock):
        pass

    def getBlock(self, address: Address):
        pass

