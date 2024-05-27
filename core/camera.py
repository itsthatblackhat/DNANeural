from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

class Camera:
    def __init__(self, display):
        self.display = display
        self.angle = [0, 0]
        self.distance = 5
        self.mouse_sensitivity = 0.2
        self.zoom_sensitivity = 0.1

    def update(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -self.distance)
        glRotatef(self.angle[0], 1, 0, 0)
        glRotatef(self.angle[1], 0, 1, 0)
        glMatrixMode(GL_MODELVIEW)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                self.angle[0] += event.rel[1] * self.mouse_sensitivity
                self.angle[1] += event.rel[0] * self.mouse_sensitivity
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.distance -= self.zoom_sensitivity
            elif event.button == 5:
                self.distance += self.zoom_sensitivity
