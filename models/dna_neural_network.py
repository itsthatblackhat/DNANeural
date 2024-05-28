import numpy as np
from OpenGL.GL import *
from OpenGL.GL import glBegin, glEnd, glVertex3fv, glColor3f
from pyglet.gl import GL_LINES

from models.neural_network import NeuralNetwork

class DNANeuralNetwork:
    def __init__(self, neurons, coord_manager):
        self.neurons = neurons
        self.coord_manager = coord_manager
        self.synapses = self.initialize_synapses()
        self.neural_network = NeuralNetwork()
        print(f"DNANeuralNetwork initialized with neurons: {self.neurons}")

    def initialize_synapses(self):
        synapses = []
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons)):
                if i != j and np.random.rand() < 0.3:
                    synapses.append((self.neurons[i], self.neurons[j]))
        return synapses

    def update(self, dt):
        for neuron in self.neurons:
            neuron.update(dt)
        self.neural_network.update(dt)  # Update neural network
        print(f"DNANeuralNetwork update called with dt: {dt}")

    def draw(self, renderer):
        for neuron in self.neurons:
            neuron.draw(renderer)
        self.draw_synapses()
        print("Synapses drawn")

    def draw_synapses(self):
        glBegin(GL_LINES)
        for (start, end) in self.synapses:
            glColor3f(1.0, 1.0, 1.0)
            glVertex3fv(start.position)
            glVertex3fv(end.position)
        glEnd()
