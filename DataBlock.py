
class DataBlock:

    def __init__(self, size, data_value=None):
        self.size = size
        self.default_data_value = data_value
        self.num_blocks = size // 8  # e.g. 8 doubles in example
        self.data = self.num_blocks * [data_value]

    def get_value(self, offset):
        return self.data[offset]

    def set_value(self, offset, value):
        self.data[offset] = value

    def print_data(self):
        print(self.data)
