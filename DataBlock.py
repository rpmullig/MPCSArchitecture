class DataBlock:
    size: int
    data: [float]

    def __init__(self, size: int):
        self.size = size
        self.data = [float() for x in range(0, self.size)]  # floats in Python are doubles in C
