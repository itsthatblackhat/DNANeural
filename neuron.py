import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Neuron:
    def __init__(self, position, color, neuron_type):
        self.position = np.array(position, dtype='float32')
        self.color = np.array(color, dtype='float32')
        self.velocity = np.random.uniform(-0.01, 0.01, size=3)
        self.activated = False
        self.dendrites = []
        self.axons = []
        self.neuron_type = neuron_type  # Add neuron type

    def add_dendrite(self, dendrite):
        self.dendrites.append(dendrite)

    def add_axon(self, axon):
        self.axons.append(axon)

    def receive_input(self, input_signal):
        if np.random.rand() < input_signal:
            self.activated = True
            self.color = np.array([1.0, 0.0, 0.0], dtype='float32')  # Change color to red to indicate activation

    def generate_action_potential(self):
        if self.activated:
            for axon in self.axons:
                axon.transmit_signal()

    def update(self):
        if self.activated:
            self.position += self.velocity
            for i in range(3):
                if self.position[i] > 1 or self.position[i] < -1:
                    self.velocity[i] = -self.velocity[i]
            self.activated = False

    def draw(self, renderer):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3fv(self.color)
        if self.neuron_type == 'sphere':
            vertices, normals, colors = renderer.generate_sphere(0.1, 10, 10)
            renderer.render_sphere(vertices, normals, colors)
        elif self.neuron_type == 'triangle':
            renderer.render_triangle()
        elif self.neuron_type == 'quad':
            renderer.render_quad()
        elif self.neuron_type == 'line':
            renderer.render_line()
        elif self.neuron_type == 'point':
            renderer.render_point()
        glPopMatrix()
