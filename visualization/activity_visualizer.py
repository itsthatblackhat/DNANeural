import pygame
from OpenGL.GL import *
from OpenGL.raw.GLU import gluPerspective

from models.dna_neural_network import DNANeuralNetwork
from neuron import Neuron
from visualization.coordinate_manager import CoordinateManager
from visualization.shader_sphere import ShaderSphereRenderer

class ActivityVisualizer:
    def __init__(self, dna_network):
        self.dna_network = dna_network
        self.renderer = ShaderSphereRenderer()
        print("ActivityVisualizer created with DNANeuralNetwork and ShaderSphereRenderer")


    def update(self, dt):
        self.dna_network.update(dt)

    def render(self):
        self.dna_network.draw(self.renderer)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    coord_manager = CoordinateManager()
    neurons = [
        Neuron((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), 'sphere', coord_manager),
        Neuron((1.0, 1.0, 1.0), (0.0, 1.0, 0.0), 'sphere', coord_manager),
        Neuron((-1.0, -1.0, -1.0), (0.0, 0.0, 1.0), 'sphere', coord_manager)
    ]
    dna_network = DNANeuralNetwork(neurons, coord_manager)
    visualizer = ActivityVisualizer(dna_network)
    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick() / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        visualizer.update(dt)
        visualizer.render()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
