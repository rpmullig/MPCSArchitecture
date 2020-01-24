class Address:
    """
    Holds a memory address
    """
    address: int    # Entire address
    tag: int        # Address tag
    index: int      # Address index
    off_set: int      # Offset

    def __init__(self, address: int, num_mask_index: int, num_mask_offset: int) -> None:
        """
        :param address: Full address
        :param num_mask_index: Number of bits used for index
        :param num_mask_offset: Number of bits used for offset
        """
        self.address = address
        self.off_set = address & ((2**num_mask_offset) - 1)             # get lower num_mask_offset number of bits
        self.index = (address >> num_mask_offset) % (2**num_mask_index)  # Get middle bits needed for index
        self.tag = address >> (num_mask_offset + num_mask_index)

    def get_tag(self) -> int:
        return self.tag

    def get_index(self) -> int:
        return self.index

    def get_offset(self) -> int:
        return self.off_set
