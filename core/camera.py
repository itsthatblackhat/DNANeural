from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

class Camera:
    def __init__(self, display):
        self.display = display
        self.angle = [0, 0]
        self.position = [0, 0, 5]
        self.mouse_sensitivity = 0.2
        self.move_sensitivity = 0.2
        self.zoom_sensitivity = 0.1
        self.keys = {
            pygame.K_w: False,
            pygame.K_s: False,
            pygame.K_a: False,
            pygame.K_d: False,
            pygame.K_SPACE: False,
            pygame.K_c: False,
            pygame.K_q: False,
            pygame.K_e: False,
        }

    def update(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 1000.0)  # Increased far clipping plane
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])
        glRotatef(self.angle[0], 1, 0, 0)
        glRotatef(self.angle[1], 0, 1, 0)
        glMatrixMode(GL_MODELVIEW)

        # Handle continuous motion based on pressed keys
        if self.keys[pygame.K_w]:
            self.position[2] -= self.move_sensitivity
        if self.keys[pygame.K_s]:
            self.position[2] += self.move_sensitivity
        if self.keys[pygame.K_a]:
            self.position[0] -= self.move_sensitivity
        if self.keys[pygame.K_d]:
            self.position[0] += self.move_sensitivity
        if self.keys[pygame.K_SPACE]:
            self.position[1] += self.move_sensitivity
        if self.keys[pygame.K_c]:
            self.position[1] -= self.move_sensitivity
        if self.keys[pygame.K_q]:
            self.angle[1] -= self.mouse_sensitivity * 5
        if self.keys[pygame.K_e]:
            self.angle[1] += self.mouse_sensitivity * 5

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                self.angle[0] += event.rel[1] * self.mouse_sensitivity
                self.angle[1] += event.rel[0] * self.mouse_sensitivity
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.position[2] -= self.zoom_sensitivity
            elif event.button == 5:
                self.position[2] += self.zoom_sensitivity
        if event.type == pygame.KEYDOWN:
            if event.key in self.keys:
                self.keys[event.key] = True
        if event.type == pygame.KEYUP:
            if event.key in self.keys:
                self.keys[event.key] = False
