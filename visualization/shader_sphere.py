from OpenGL.GL import *
from math import sin, cos, pi

from OpenGL.GLU import gluNewQuadric
from OpenGL.raw.GLU import gluSphere


class ShaderSphereRenderer:
    def __init__(self):
        pass

    def render_sphere(self, color, radius=1.0, slices=16, stacks=16):
        quadric = gluNewQuadric()
        gluSphere(quadric, radius, slices, stacks)

        glColor3f(*color)
        num_lats = 20
        num_longs = 20
        radius = 1.0


        for i in range(0, num_lats + 1):
            lat0 = pi * (-0.5 + float(i - 1) / num_lats)
            z0 = sin(lat0)
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(i) / num_lats)
            z1 = sin(lat1)
            zr1 = cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(0, num_longs + 1):
                lng = 2 * pi * float(j - 1) / num_longs
                x = cos(lng)
                y = sin(lng)

                glVertex3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()
