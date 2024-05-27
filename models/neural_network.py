import tensorflow as tf
from tensorflow.keras import layers, models

class NeuralNetwork:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = models.Sequential()
        model.add(layers.Input(shape=(4,)))  # Example input shape
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(4, activation='softmax'))  # Example output shape
        return model

    def train(self, data, labels):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(data, labels, epochs=10)

    def predict(self, data):
        return self.model.predict(data)
