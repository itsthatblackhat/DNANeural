import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import svgpathtools as svg

class Neuron:
    def __init__(self, position, color, neuron_type, coord_manager, svg_file):
        self.position = np.array(position, dtype='float32')
        self.color = np.array(color, dtype='float32')
        self.velocity = np.random.uniform(-0.01, 0.01, size=3)
        self.activated = False
        self.dendrites = []
        self.axons = []
        self.neuron_type = neuron_type
        self.coord_manager = coord_manager
        self.shape_id = id(self)
        self.svg_file = svg_file
        self.path_data = self.load_svg(svg_file)
        self.init_position()
        print(f"Neuron initialized at {position} with color {color} and type {neuron_type}")

    def load_svg(self, filename):
        paths, attributes = svg.svg2paths(filename)
        return paths

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
        glScalef(0.001, 0.001, 0.001)  # Adjusting scale for all neurons
        self.draw_svg_path()
        glPopMatrix()

    def draw_svg_path(self):
        glColor3f(*self.color)
        glBegin(GL_LINES)
        for path in self.path_data:
            for segment in path:
                if isinstance(segment, svg.path.CubicBezier):
                    points = [segment.start, segment.control1, segment.control2, segment.end]
                    for point in points:
                        glVertex2f(point.real, point.imag)
        glEnd()

    def init_position(self):
        if self.shape_id not in self.coord_manager.positions:
            self.coord_manager.update_position(self.shape_id, (0.0, 0.0, 0.0))
