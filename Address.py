class Address:
    """
    Holds a memory address
    """
    address: float    # Entire address
    block_number: int
    block_offset: int
    block_tag: int
    block_index: int

    def __init__(self, address: float, block_size: int, num_sets: int) -> None:
        """
        :param address:
        :param block_size:
        :param num_sets:
        """
        self.address = address
        doubles_per_block = block_size // 8
        self.block_number = int(address / doubles_per_block)
        self.block_offset = int(address % doubles_per_block)
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
