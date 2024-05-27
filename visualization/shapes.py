from OpenGL.GL import *
from math import sin, cos, pi
import numpy as np
from visualization.physics import PhysicsObject

class Shape:
    def __init__(self, color, shape_id, coord_manager):
        self.color = color
        self.shape_id = shape_id
        self.coord_manager = coord_manager
        self.physics = PhysicsObject(self)
        self.init_position()

    def draw(self):
        pass

    def apply_transformations(self):
        transformation_matrix = self.coord_manager.get_transformation_matrix(self.shape_id)
        glPushMatrix()
        glMultMatrixf(transformation_matrix.T)

    def reset_transformations(self):
        glPopMatrix()

    def init_position(self):
        if self.shape_id not in self.coord_manager.positions:
            self.coord_manager.update_position(self.shape_id, (0.0, 0.0, 0.0))

class Point(Shape):
    def __init__(self, x, y, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)
        self.x = x
        self.y = y
        self.coord_manager.update_position(shape_id, (x, y, 0.0))

    def draw(self):
        self.apply_transformations()
        glBegin(GL_POINTS)
        glColor3f(*self.color)
        glVertex3f(self.x, self.y, 0.0)
        glEnd()
        self.reset_transformations()

class Line(Shape):
    def __init__(self, start, end, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)
        self.start = start
        self.end = end
        self.coord_manager.update_position(shape_id, start)

    def draw(self):
        self.apply_transformations()
        glBegin(GL_LINES)
        glColor3f(*self.color)
        glVertex3f(*self.start)
        glVertex3f(*self.end)
        glEnd()
        self.reset_transformations()

class Triangle(Shape):
    def __init__(self, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)

    def draw(self):
        self.apply_transformations()
        glBegin(GL_TRIANGLES)
        glColor3f(*self.color)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()
        self.reset_transformations()

class Square(Shape):
    def __init__(self, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)

    def draw(self):
        self.apply_transformations()
        glBegin(GL_QUADS)
        glColor3f(*self.color)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glEnd()
        self.reset_transformations()

class Cube(Shape):
    def __init__(self, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)

    def draw(self):
        self.apply_transformations()
        vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ]

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        glBegin(GL_LINES)
        glColor3f(*self.color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
        self.reset_transformations()

class Sphere(Shape):
    def __init__(self, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)

    def draw(self):
        self.apply_transformations()
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
            glColor3f(*self.color)
            for j in range(0, num_longs + 1):
                lng = 2 * pi * float(j - 1) / num_longs
                x = cos(lng)
                y = sin(lng)

                glVertex3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()
        self.reset_transformations()

class Pyramid(Shape):
    def __init__(self, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)

    def draw(self):
        self.apply_transformations()
        glBegin(GL_TRIANGLES)
        glColor3f(*self.color)
        # Front
        glNormal3f(0.0, 0.5, 0.5)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        # Right
        glNormal3f(0.5, 0.5, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        # Back
        glNormal3f(0.0, 0.5, -0.5)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        # Left
        glNormal3f(-0.5, 0.5, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glEnd()
        self.reset_transformations()

class Circle(Shape):
    def __init__(self, x, y, radius, color, shape_id, coord_manager):
        super().__init__(color, shape_id, coord_manager)
        self.x = x
        self.y = y
        self.radius = radius
        self.coord_manager.update_position(shape_id, (x, y, 0.0))

    def draw(self):
        self.apply_transformations()
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(*self.color)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex2f(self.x, self.y)
        for i in range(361):
            angle = 2 * pi * i / 360
            glVertex2f(self.x + cos(angle) * self.radius, self.y + sin(angle) * self.radius)
        glEnd()
        self.reset_transformations()
