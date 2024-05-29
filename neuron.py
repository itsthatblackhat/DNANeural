import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Neuron:
    def __init__(self, position, color, neuron_type, coord_manager):
        self.position = np.array(position, dtype='float32')
        self.color = np.array(color, dtype='float32')
        self.velocity = np.random.uniform(-0.01, 0.01, size=3)
        self.activated = False
        self.dendrites = []
        self.axons = []
        self.neuron_type = neuron_type
        self.coord_manager = coord_manager
        self.shape_id = id(self)
        self.init_position()
        print(f"Neuron initialized at {position} with color {color} and type {neuron_type}")

    def add_dendrite(self, dendrite):
        self.dendrites.append(dendrite)

    def add_axon(self, axon):
        self.axons.append(axon)

    def receive_input(self, input_signal):
        if np.random.rand() < input_signal:
            self.activated = True
            self.color = np.array([1.0, 0.0, 0.0], dtype='float32')

    def generate_action_potential(self):
        if self.activated:
            for axon in self.axons:
                axon.transmit_signal()

    def update(self, dt):
        if self.activated:
            self.position += self.velocity * dt
            for i in range(3):
                if self.position[i] > 1 or self.position[i] < -1:
                    self.velocity[i] = -self.velocity[i]
            self.activated = False

    def draw(self, renderer):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3fv(self.color)
        self.draw_soma()
        self.draw_dendrites()
        self.draw_axon()
        glPopMatrix()

    def draw_soma(self):
        glColor3fv(self.color)
        quad = gluNewQuadric()
        gluSphere(quad, 0.2, 20, 20)
        gluDeleteQuadric(quad)

    def draw_dendrites(self):
        glColor3fv((0.0, 1.0, 0.0))
        for _ in range(5):
            angle = np.random.uniform(0, 2 * np.pi)
            length = np.random.uniform(0.2, 0.5)
            glBegin(GL_LINES)
            glVertex3fv(self.position)
            glVertex3fv(self.position + np.array([np.cos(angle) * length, np.sin(angle) * length, 0.0]))
            glEnd()

    def draw_axon(self):
        glColor3fv((0.0, 0.0, 1.0))
        glPushMatrix()
        glTranslatef(0.0, -0.2, 0.0)
        quad = gluNewQuadric()
        gluCylinder(quad, 0.05, 0.05, 1.0, 20, 20)
        gluDeleteQuadric(quad)
        glPopMatrix()

    def init_position(self):
        if self.shape_id not in self.coord_manager.positions:
            self.coord_manager.update_position(self.shape_id, (0.0, 0.0, 0.0))
