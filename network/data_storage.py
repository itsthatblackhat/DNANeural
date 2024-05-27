import json
import h5py

class DataStorage:
    def __init__(self, sequence_file, weight_file):
        self.sequence_file = sequence_file
        self.weight_file = weight_file

    def save_sequence(self, sequences):
        with open(self.sequence_file, 'w') as file:
            json.dump({'sequences': sequences}, file)

    def load_sequences(self):
        with open(self.sequence_file, 'r') as file:
            return json.load(file)['sequences']

    def save_weights(self, model):
        model.save_weights(self.weight_file)

    def load_weights(self, model):
        model.load_weights(self.weight_file)
