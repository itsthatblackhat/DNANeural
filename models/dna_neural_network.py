import numpy as np
from OpenGL.GL import *
from ctypes import c_float

class DNANeuralNetwork:
    def __init__(self, neurons, coord_manager):
        self.neurons = neurons
        self.coord_manager = coord_manager
        self.synapses = self.initialize_synapses()
        print(f"DNANeuralNetwork initialized with neurons: {neurons}")

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

    def draw(self, renderer):
        for neuron in self.neurons:
            neuron.draw(renderer)
        self.draw_synapses()

    def draw_synapses(self):
        glBegin(GL_LINES)
        for start_neuron, end_neuron in self.synapses:
            start_pos = np.array(start_neuron.position, dtype=c_float)
            end_pos = np.array(end_neuron.position, dtype=c_float)
            glVertex3fv(start_pos)
            glVertex3fv(end_pos)
        glEnd()

    def propagate_signals(self):
        for neuron in self.neurons:
            neuron.update()
            neuron.generate_action_potential()
