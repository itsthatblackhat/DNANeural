import json

class InputHandler:
    def __init__(self, sequence_file):
        self.sequence_file = sequence_file
        self.load_sequences()

    def load_sequences(self):
        with open(self.sequence_file, 'r') as file:
            self.sequences = json.load(file)

    def get_sequence(self, key):
        return self.sequences.get(key, None)
