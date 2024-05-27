import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit

class TriangleRenderer:
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

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)
        print("Rendered triangle")

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
    renderer = TriangleRenderer()
    renderer.run()
