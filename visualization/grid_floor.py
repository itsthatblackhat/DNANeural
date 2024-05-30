from OpenGL.GL import *
from OpenGL.GLU import *

class GridFloor:
    def __init__(self, step=1, size=1000):
        self.step = step
        self.size = size

    def draw(self, camera_pos):
        glColor3f(0.0, 0.5, 0.0)  # Dark green color
        glBegin(GL_LINES)
        for i in range(-self.size, self.size + 1, self.step):
            glVertex3f(i, 0, -self.size + camera_pos[2])
            glVertex3f(i, 0, self.size + camera_pos[2])
            glVertex3f(-self.size + camera_pos[0], 0, i)
            glVertex3f(self.size + camera_pos[0], 0, i)
        glEnd()
