import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from visualization.shapes import Point, Line, Triangle, Square, Cube, Sphere, Pyramid, Circle
from visualization.coordinate_manager import CoordinateManager
from core.camera import Camera

def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def main():
    init()
    display = (800, 600)
    coord_manager = CoordinateManager()
    shapes = [
        Point(0.0, 0.0, (1.0, 0.0, 0.0), 1, coord_manager),
        Line((0.0, 0.0, 0.0), (1.0, 1.0, 1.0), (0.0, 1.0, 0.0), 2, coord_manager),
        Triangle((0.0, 0.0, 1.0), 3, coord_manager),
        Square((1.0, 0.5, 0.0), 4, coord_manager),
        Cube((1.0, 1.0, 1.0), 5, coord_manager),
        Sphere((0.0, 1.0, 1.0), 6, coord_manager),
        Pyramid((1.0, 0.0, 1.0), 7, coord_manager),
        Circle(x=0.0, y=0.0, radius=1, color=(1.0, 1.0, 0.0), shape_id=8, coord_manager=coord_manager)
    ]

    coord_manager.update_position(1, (0.0, 2.0, 0.0))
    coord_manager.update_position(2, (-3.0, 0.0, 0.0))
    coord_manager.update_position(3, (3.0, 0.0, 0.0))
    coord_manager.update_position(4, (0.0, -3.0, 0.0))
    coord_manager.update_position(5, (0.0, 0.0, -3.0))
    coord_manager.update_position(6, (3.0, 3.0, 0.0))
    coord_manager.update_position(7, (-3.0, 3.0, 0.0))
    coord_manager.update_position(8, (0.0, 0.0, 3.0))

    camera = Camera(display=display)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            camera.handle_event(event)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            camera.distance -= camera.zoom_sensitivity
        if keys[pygame.K_s]:
            camera.distance += camera.zoom_sensitivity
        if keys[pygame.K_a]:
            camera.angle[1] -= camera.mouse_sensitivity
        if keys[pygame.K_d]:
            camera.angle[1] += camera.mouse_sensitivity
        if keys[pygame.K_q]:
            camera.angle[0] -= camera.mouse_sensitivity
        if keys[pygame.K_e]:
            camera.angle[0] += camera.mouse_sensitivity

        camera.update()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for shape in shapes:
            shape.draw()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
