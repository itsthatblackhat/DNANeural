import numpy as np
from OpenGL.GL import *
from math import sin, cos, pi

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
        self.draw_cell_body()
        self.draw_dendrites()
        self.draw_axon()
        glPopMatrix()

    def draw_cell_body(self):
        # Draw the cell body (soma)
        glColor3fv(self.color)
        num_lats = 10
        num_longs = 10
        radius = 0.5

        for i in range(0, num_lats + 1):
            lat0 = pi * (-0.5 + float(i - 1) / num_lats)
            z0 = sin(lat0)
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(i) / num_lats)
            z1 = sin(lat1)
            zr1 = cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(0, num_longs + 1):
                lng = 2 * pi * float(j - 1) / num_longs
                x = cos(lng)
                y = sin(lng)

                glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)
                glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
            glEnd()

    def draw_dendrites(self):
        # Draw simple dendrites as lines for now
        glColor3f(0.6, 0.4, 0.2)
        glBegin(GL_LINES)
        for _ in range(10):
            angle = np.random.uniform(0, 2 * pi)
            glVertex3f(0, 0, 0)
            glVertex3f(sin(angle) * 1.5, cos(angle) * 1.5, np.random.uniform(-1, 1))
        glEnd()

    def draw_axon(self):
        # Draw a simple axon as a line for now
        glColor3f(0.8, 0.8, 0.8)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, -2, 0)
        glEnd()

    def init_position(self):
        if self.shape_id not in self.coord_manager.positions:
            self.coord_manager.update_position(self.shape_id, (0.0, 0.0, 0.0))
