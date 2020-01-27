class DataBlock:

    def __init__(self, size, default_data_value):
        """
        :param size: block size (e.g. 64 bytes means 8 doubles)
        :param default_data_value:
        """
        self.size = size
        self.default_data_value = default_data_value
        self.num_blocks = size // 8                             # e.g. 8 doubles in example
        self.data = self.num_blocks * [default_data_value]

    def get_value(self, index):
        return self.data[index]

    def set_value(self, index, value):
        self.data[index] = value

    def print_data(self):
        print(self.data)
