class Address:
    """
    Holds a memory address and it's corresponding block number, tag, index, and offset
    """

    def __init__(self, address, block_size, num_sets):
        self.address = address
        doubles_per_block = int(block_size // 8)
        self.block_number = int(address // doubles_per_block)
        self.block_offset = int(self.address % doubles_per_block)
        self.block_tag = int(self.block_number / num_sets)
        self.block_index = int(self.block_number % num_sets)

    def set_offset(self, offset: int):
        self.block_tag = offset

    def get_offset(self) -> int:
        return self.block_offset

    def get_tag(self) -> int:
        return self.block_tag

    def get_index(self) -> int:
        return self.block_index

    def get_block_number(self):
        return self.block_number

    def get_address(self):
        return self.address

    def set_address(self, address, block_size, num_sets):
        self.address = address
        doubles_per_block = int(block_size // 8)
        self.block_number = int(address // doubles_per_block)
        self.block_offset = int(self.address % doubles_per_block)
        self.block_tag = int(self.block_number / num_sets)
        self.block_index = int(self.block_number % num_sets)