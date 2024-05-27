from OpenGL.GL import *
import numpy as np
import random

class ParticleSystem:
    def __init__(self, num_particles):
        self.num_particles = num_particles
        self.positions = np.random.uniform(-1, 1, (num_particles, 3)).astype(np.float32)
        self.colors = np.random.uniform(0, 1, (num_particles, 3)).astype(np.float32)

    def update(self):
        # Update particle positions and colors if needed
        pass

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0, self.positions)
        glColorPointer(3, GL_FLOAT, 0, self.colors)

        glDrawArrays(GL_POINTS, 0, self.num_particles)

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

        print(f"Rendered {self.num_particles} particles")
