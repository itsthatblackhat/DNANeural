# particle_system.py
from OpenGL.GL import *
from random import uniform

class ParticleSystem:
    def __init__(self, coord_manager):
        self.coord_manager = coord_manager
        self.particles = self.create_particles(100)  # Create 100 particles

    def create_particles(self, count):
        particles = []
        for _ in range(count):
            position = [uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]
            color = [uniform(0, 1), uniform(0, 1), uniform(0, 1)]
            particles.append({'position': position, 'color': color})
        return particles

    def update(self, dt):
        for particle in self.particles:
            # Update particle positions or other properties here if needed
            pass

    def render(self):
        glBegin(GL_POINTS)
        for particle in self.particles:
            glColor3fv(particle['color'])
            glVertex3fv(particle['position'])
        glEnd()
