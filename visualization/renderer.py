import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

vertex_shader_code = """
#version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;
out vec3 fragColor;
void main() {
    fragColor = color;
    gl_Position = vec4(position, 1.0);
}
"""

fragment_shader_code = """
#version 330 core
in vec3 fragColor;
out vec4 color;
void main() {
    color = vec4(fragColor, 1.0);
}
"""

class Renderer:
    def __init__(self):
        self.init_shaders()
        self.init_lighting()

    def init_shaders(self):
        self.vertex_shader = compileShader(vertex_shader_code, GL_VERTEX_SHADER)
        self.fragment_shader = compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)
        self.shader_program = compileProgram(self.vertex_shader, self.fragment_shader)
        glUseProgram(self.shader_program)

    def init_lighting(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        light_pos = [0.0, 0.0, 1.0, 0.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
        light_color = [1.0, 1.0, 1.0, 1.0]
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_color)

    def render(self, scene):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.shader_program)  # Use the shader program
        scene.render()
        pygame.display.flip()
        pygame.time.wait(10)
