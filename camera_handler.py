import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self, display):
        self.position = [0, 0, -5]
        self.rotation = [0, 0]
        self.speed = 0.1
        self.sensitivity = 0.2
        self.display = display

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.position[2] += self.speed
            elif event.key == pygame.K_s:
                self.position[2] -= self.speed
            elif event.key == pygame.K_a:
                self.position[0] += self.speed
            elif event.key == pygame.K_d:
                self.position[0] -= self.speed
            elif event.key == pygame.K_SPACE:
                self.position[1] += self.speed
            elif event.key == pygame.K_c:
                self.position[1] -= self.speed
            elif event.key == pygame.K_q:
                self.rotation[1] -= self.sensitivity
            elif event.key == pygame.K_e:
                self.rotation[1] += self.sensitivity

    def update(self):
        glLoadIdentity()
        glRotatef(self.rotation[1], 0, 1, 0)
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])
