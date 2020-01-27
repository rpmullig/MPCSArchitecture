import DataBlock
import Address


class Cache:
    numSet: int
    numBlocks: int

    def __init__(self, numSet, numBlocks):
        self.numSet = numSet
        self.numBlocks = numBlocks
        self.blocks = [DataBlock(numSet) for x in range(0, numBlocks)]

    def getDouble(self, address: Address):
        pass

    def setDouble(self, address: Address, value: float):
        pass

    def getBlock(self, address: Address):
        pass

    def setBlock(self, address: Address, block: DataBlock):
        pass
