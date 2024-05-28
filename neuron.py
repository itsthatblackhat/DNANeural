import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from visualization.shader_sphere import ShaderSphereRenderer
from visualization.physics import PhysicsObject

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
            self.coord_manager.update_position(self.shape_id, self.position)

    def draw(self, renderer):
        transformation_matrix = self.coord_manager.get_transformation_matrix(self.shape_id)
        glPushMatrix()
        glMultMatrixf(transformation_matrix.T)
        renderer.render_sphere(self.color)
        glPopMatrix()

    def init_position(self):
        if self.shape_id not in self.coord_manager.positions:
            self.coord_manager.update_position(self.shape_id, self.position)
