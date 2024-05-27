import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit
import numpy as np

def draw_sphere(radius, slices, stacks):
    for i in range(slices):
        lat0 = np.pi * (-0.5 + float(i) / slices)
        z0 = radius * np.sin(lat0)
        zr0 = radius * np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(i + 1) / slices)
        z1 = radius * np.sin(lat1)
        zr1 = radius * np.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(stacks + 1):
            lng = 2 * np.pi * float(j) / stacks
            x = np.cos(lng)
            y = np.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

class SphereRenderer:
    def __init__(self):
        pygame.init()
        glutInit()
        display = (800, 600)
        self.screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        glColor3f(0.0, 1.0, 0.0)
        draw_sphere(1, 20, 20)

        pygame.display.flip()
        pygame.time.wait(10)
        print("Rendered custom sphere")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run(self):
        while True:
            self.handle_events()
            self.render()

if __name__ == "__main__":
    renderer = SphereRenderer()
    renderer.run()
