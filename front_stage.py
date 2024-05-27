import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from visualization.shapes import Point, Line, Triangle, Square, Cube, Sphere, Pyramid, Circle
from visualization.coordinate_manager import CoordinateManager
from visualization.particle_system import ParticleSystem

def init():
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
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 10, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))

def main():
    init()
    coord_manager = CoordinateManager()

    # Create shapes with specific IDs and assign them to the coordinate manager
    shapes = [
        Cube((1.0, 0.0, 0.0), 1, coord_manager),
        Sphere((1.0, 1.0, 0.0), 2, coord_manager),
        Triangle((0.0, 0.0, 1.0), 3, coord_manager),
        Pyramid((1.0, 0.0, 1.0), 4, coord_manager),
        Circle(1.0, 1.0, 1.0, (0.0, 1.0, 1.0), 5, coord_manager),
        Square((1.0, 0.5, 0.0), 6, coord_manager)
    ]

    # Updating initial positions for better spacing
    coord_manager.update_position(1, (-3.0, 0.0, 0.0))  # Cube
    coord_manager.update_position(2, (3.0, 0.0, 0.0))   # Sphere
    coord_manager.update_position(3, (0.0, 3.0, 0.0))   # Triangle
    coord_manager.update_position(4, (0.0, -3.0, 0.0))  # Pyramid
    coord_manager.update_position(5, (3.0, 3.0, 0.0))   # Circle
    coord_manager.update_position(6, (-3.0, -3.0, 0.0)) # Square

    # Debugging: Print positions to verify they are set correctly
    for shape_id, position in coord_manager.positions.items():
        print(f"Shape ID {shape_id} initial position: {position}")

    particle_system = ParticleSystem()

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        for shape in shapes:
            shape.draw()

        particle_system.update(dt)
        particle_system.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
