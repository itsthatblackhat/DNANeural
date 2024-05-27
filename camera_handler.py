# camera_handler.py
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class CameraHandler:
    def __init__(self):
        self.angle = 0
        self.distance = 10
        self.height = 5
        self.mouse_sensitivity = 0.1
        self.scroll_sensitivity = 1
        self.key_sensitivity = 0.1
        self.mouse_down = False
        self.last_mouse_pos = (0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.height += self.key_sensitivity
        if keys[K_s]:
            self.height -= self.key_sensitivity
        if keys[K_a]:
            self.angle -= self.key_sensitivity
        if keys[K_d]:
            self.angle += self.key_sensitivity
        if keys[K_q]:
            self.distance += self.key_sensitivity
        if keys[K_e]:
            self.distance -= self.key_sensitivity

        glLoadIdentity()
        gluLookAt(
            self.distance * np.sin(np.radians(self.angle)), self.height, self.distance * np.cos(np.radians(self.angle)),
            0, 0, 0,
            0, 1, 0
        )

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_down = True
                self.last_mouse_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_down = False
        elif event.type == MOUSEMOTION:
            if self.mouse_down:
                x, y = event.rel
                self.angle += x * self.mouse_sensitivity
                self.height += y * self.mouse_sensitivity
        elif event.type == MOUSEWHEEL:
            self.distance -= event.y * self.scroll_sensitivity
