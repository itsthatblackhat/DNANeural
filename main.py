import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame import DOUBLEBUF, OPENGL

from visualization.shapes import Point, Line, Triangle, Square, Cube, Sphere, Pyramid, Circle
from visualization.coordinate_manager import CoordinateManager
from visualization.particle_system import ParticleSystem
from core.camera import Camera  # Ensure Camera is correctly imported


def update_physics(objects, dt):
    for obj in objects:
        obj.physics.update(dt)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    coord_manager = CoordinateManager()

    shapes = [
        Cube(color=(1.0, 0.0, 0.0), shape_id=1, coord_manager=coord_manager),
        Triangle(color=(0.0, 1.0, 0.0), shape_id=2, coord_manager=coord_manager),
        Circle(x=0.0, y=0.0, radius=1, color=(0.0, 0.0, 1.0), shape_id=3, coord_manager=coord_manager)
    ]

    coord_manager.update_position(1, (-2.0, 0.0, -10.0))
    coord_manager.update_position(2, (2.0, 0.0, -10.0))
    coord_manager.update_position(3, (0.0, 0.0, -5.0))

    particle_system = ParticleSystem(coord_manager, num_particles=100)

    clock = pygame.time.Clock()
    running = True

    camera = Camera(display)  # Initialize Camera

    while running:
        dt = clock.tick() / 1000.0  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            camera.handle_event(event)  # Handle camera events

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        camera.update()

        update_physics(shapes, dt)
        particle_system.update(dt)

        for shape in shapes:
            shape.draw()

        particle_system.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
