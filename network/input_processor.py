import numpy as np

class InputProcessor:
    def __init__(self):
        self.mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}

    def process_input(self, raw_input):
        encoded_input = [self.mapping[base] for base in raw_input]
        return np.array(encoded_input)
