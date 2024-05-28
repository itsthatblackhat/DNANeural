from OpenGL.GL import *
from OpenGL.GLU import *

class NeuronRenderer:
    def __init__(self):
        pass

    def render_sphere(self):
        quadric = gluNewQuadric()
        gluSphere(quadric, 0.1, 20, 20)
        gluDeleteQuadric(quadric)
