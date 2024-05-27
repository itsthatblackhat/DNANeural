import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

class Visualizer:
    def __init__(self):
        pygame.init()
        display = (800, 600)
        self.screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        self.neurons = []
        self.synapses = []

    def add_neuron(self, position, color):
        neuron = {'position': np.array(position, dtype='float32'), 'color': color}
        self.neurons.append(neuron)

    def add_synapse(self, start_pos, end_pos, color):
        synapse = {'start': np.array(start_pos, dtype='float32'), 'end': np.array(end_pos, dtype='float32'), 'color': color}
        self.synapses.append(synapse)

    def render_neurons(self):
        glPointSize(10)
        glBegin(GL_POINTS)
        for neuron in self.neurons:
            glColor3fv(neuron['color'])
            glVertex3fv(neuron['position'])
        glEnd()

    def render_synapses(self):
        glBegin(GL_LINES)
        for synapse in self.synapses:
            glColor3fv(synapse['color'])
            glVertex3fv(synapse['start'])
            glVertex3fv(synapse['end'])
        glEnd()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.render_neurons()
        self.render_synapses()
        pygame.display.flip()
        pygame.time.wait(10)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.render()
