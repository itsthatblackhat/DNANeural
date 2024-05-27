import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Engine:
    def __init__(self):
        pygame.init()
        display = (800, 600)
        self.screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
        glViewport(0, 0, display[0], display[1])
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])

    def run(self, render_callback):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            render_callback()
            pygame.display.flip()
            pygame.time.wait(10)
