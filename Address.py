class Address:
    """
    Holds a memory address and it's corresponding block number, tag, index, and offset
    """

    def __init__(self, address, block_size, num_sets):
        """
        :param address:
        :param block_size:
        :param num_sets:
        """
        self.address = address
        doubles_per_block = int(block_size // 8)
        self.block_number = int(address // doubles_per_block)
        self.block_offset = int(self.address % doubles_per_block)
        self.block_tag = int(self.block_number / num_sets)
        self.block_index = int(self.block_number % num_sets)

    def get_tag(self) -> int:
        """
        :return: address tag
        """
        return self.block_tag

    def get_index(self) -> int:
        """
        :return: index of address
        """
        return self.block_index

    def get_offset(self) -> int:
        """
        :return: offset of the address
        """
        return self.block_offset

    def get_block_number(self):
        """
        :return: data block number of the address
        """
        return self.block_number

    def get_address(self):
        """
        :return: returns the full address
        """
        return self.address

    def set_address(self, address, block_size, num_sets):
        """
        If not passed in to the constructor, standard setter
        :param address: The address
        :param block_size: The size of a single block
        :param num_sets: The number of sets in a block
        :return: None, adjusts the address and thus the index, tag, and offset
        """
        self.address = address
        doubles_per_block = int(block_size // 8)
        self.block_number = int(address // doubles_per_block)
        self.block_offset = int(self.address % doubles_per_block)
        self.block_tag = int(self.block_number / num_sets)
        self.block_index = int(self.block_number % num_sets)