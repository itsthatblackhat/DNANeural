import numpy as np

class OutputHandler:
    def __init__(self):
        self.reverse_mapping = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    def process_output(self, encoded_output):
        return ''.join([self.reverse_mapping[np.argmax(base)] for base in encoded_output])
