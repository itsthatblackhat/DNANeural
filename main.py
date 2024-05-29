import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame import DOUBLEBUF, OPENGL

from visualization.activity_visualizer import ActivityVisualizer
from network.input_handler import InputHandler
from models.dna_neural_network import DNANeuralNetwork
from front_stage import setup_stage
from visualization.coordinate_manager import CoordinateManager
from audio_listener import AudioListener
from camera_listener import CameraListener
from math import *

def main():
    pygame.init()
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Set up a basic display buffer (only RGB and depth)
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    print("OpenGL initialization complete")

    coord_manager = CoordinateManager()
    neurons = setup_stage(coord_manager)
    dna_network = DNANeuralNetwork(neurons, coord_manager)
    visualizer = ActivityVisualizer(dna_network)
    print("Visualizer and DNA network initialization complete")

    audio_listener = AudioListener()
    print("Audio listener initialized")

    clock = pygame.time.Clock()
    running = True
    camera_pos = [0.0, 0.0, -10.0]
    camera_rot = [0.0, 0.0]

    def handle_camera_movement(keys):
        move_speed = 0.02
        rotate_speed = 0.06

        if keys[pygame.K_w]:
            camera_pos[0] += move_speed * sin(camera_rot[1] * pi / 180)
            camera_pos[2] -= move_speed * cos(camera_rot[1] * pi / 180)
        if keys[pygame.K_s]:
            camera_pos[0] -= move_speed * sin(camera_rot[1] * pi / 180)
            camera_pos[2] += move_speed * cos(camera_rot[1] * pi / 180)
        if keys[pygame.K_a]:
            camera_pos[0] -= move_speed * cos(camera_rot[1] * pi / 180)
            camera_pos[2] -= move_speed * sin(camera_rot[1] * pi / 180)
        if keys[pygame.K_d]:
            camera_pos[0] += move_speed * cos(camera_rot[1] * pi / 180)
            camera_pos[2] += move_speed * sin(camera_rot[1] * pi / 180)
        if keys[pygame.K_SPACE]:
            camera_pos[1] -= move_speed
        if keys[pygame.K_c]:
            camera_pos[1] += move_speed
        if keys[pygame.K_q]:
            camera_rot[1] -= rotate_speed
        if keys[pygame.K_e]:
            camera_rot[1] += rotate_speed

    print("Entering main loop")

    while running:
        dt = clock.tick() / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        handle_camera_movement(keys)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(camera_rot[0], 1, 0, 0)
        glRotatef(camera_rot[1], 0, 1, 0)
        glTranslatef(-camera_pos[0], -camera_pos[1], -camera_pos[2])

        visualizer.update(dt)
        visualizer.render()

        pygame.display.flip()
        print("Frame rendered")

    audio_listener.__del__()
    pygame.quit()

if __name__ == "__main__":
    main()
