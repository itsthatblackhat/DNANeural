import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from visualization.shapes import Point, Line, Triangle, Square, Cube, Sphere, Pyramid, Circle
from visualization.coordinate_manager import CoordinateManager

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -10)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    coord_manager = CoordinateManager()

    shapes = [
        Point(0.0, 0.0, (1.0, 0.0, 0.0), "point1", coord_manager),
        Line((0.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0), "line1", coord_manager),
        Triangle((0.0, 0.0, 1.0), "triangle1", coord_manager),
        Square((1.0, 0.5, 0.0), "square1", coord_manager),
        Cube((1.0, 1.0, 1.0), "cube1", coord_manager),
        Sphere((0.0, 1.0, 1.0), "sphere1", coord_manager),
        Pyramid((1.0, 0.0, 1.0), "pyramid1", coord_manager),
        Circle(0.0, 0.0, 1.0, (1.0, 1.0, 0.0), "circle1", coord_manager)
    ]

    coord_manager.update_position("sphere1", (4.0, 0.0, 0.0))
    coord_manager.update_position("cube1", (-4.0, 0.0, 0.0))
    coord_manager.update_position("pyramid1", (0.0, -4.0, 0.0))
    coord_manager.update_position("circle1", (0.0, 4.0, 0.0))
    coord_manager.update_rotation("cube1", (0.5, 0.5, 0.0))
    coord_manager.update_scale("pyramid1", (0.5, 0.5, 0.5))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for shape in shapes:
            shape.draw()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
