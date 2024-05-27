import numpy as np
from OpenGL.GL import *
from visualization.physics import PhysicsObject

class Particle:
    def __init__(self, position, velocity, color, lifetime, coord_manager, particle_id):
        self.position = np.array(position, dtype=np.float32)
        self.velocity = np.array(velocity, dtype=np.float32)
        self.color = color
        self.lifetime = lifetime
        self.coord_manager = coord_manager
        self.shape_id = particle_id  # Ensure shape_id is set for compatibility with PhysicsObject
        self.physics = PhysicsObject(self)
        self.coord_manager.update_position(self.shape_id, self.position)

    def update(self, dt):
        self.physics.update(dt)
        self.lifetime -= dt

    def draw(self):
        self.apply_transformations()
        glColor3f(*self.color)
        glBegin(GL_POINTS)
        glVertex3f(*self.position)
        glEnd()
        self.reset_transformations()

    def apply_transformations(self):
        transformation_matrix = self.coord_manager.get_transformation_matrix(self.shape_id)
        glPushMatrix()
        glMultMatrixf(transformation_matrix.T)

    def reset_transformations(self):
        glPopMatrix()

class ParticleSystem:
    def __init__(self, coord_manager, num_particles=100):
        self.coord_manager = coord_manager
        self.particles = []
        self.num_particles = num_particles
        self.initialize_particles()

    def initialize_particles(self):
        for i in range(self.num_particles):
            position = np.random.uniform(-1.0, 1.0, 3)
            velocity = np.random.uniform(-0.1, 0.1, 3)
            color = np.random.uniform(0.5, 1.0, 3)
            lifetime = np.random.uniform(1.0, 5.0)
            particle = Particle(position, velocity, color, lifetime, self.coord_manager, i + 1000)
            self.particles.append(particle)

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)
            if particle.lifetime <= 0:
                self.reset_particle(particle)

    def reset_particle(self, particle):
        particle.position = np.random.uniform(-1.0, 1.0, 3)
        particle.velocity = np.random.uniform(-0.1, 0.1, 3)
        particle.color = np.random.uniform(0.5, 1.0, 3)
        particle.lifetime = np.random.uniform(1.0, 5.0)
        self.coord_manager.update_position(particle.shape_id, particle.position)

    def draw(self):
        for particle in self.particles:
            particle.draw()
