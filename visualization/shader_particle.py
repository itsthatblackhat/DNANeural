import pygame
from OpenGL.GL import *
import numpy as np

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

class ShaderParticleRenderer:
    def __init__(self):
        self.init_shaders()
        self.init_particles()

    def init_shaders(self):
        self.vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(self.vertex_shader, vertex_shader_code)
        glCompileShader(self.vertex_shader)

        if not glGetShaderiv(self.vertex_shader, GL_COMPILE_STATUS):
            print(glGetShaderInfoLog(self.vertex_shader))
            raise RuntimeError("Vertex shader compilation error")

        self.fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(self.fragment_shader, fragment_shader_code)
        glCompileShader(self.fragment_shader)

        if not glGetShaderiv(self.fragment_shader, GL_COMPILE_STATUS):
            print(glGetShaderInfoLog(self.fragment_shader))
            raise RuntimeError("Fragment shader compilation error")

        self.shader_program = glCreateProgram()
        glAttachShader(self.shader_program, self.vertex_shader)
        glAttachShader(self.shader_program, self.fragment_shader)
        glLinkProgram(self.shader_program)

        if not glGetProgramiv(self.shader_program, GL_LINK_STATUS):
            print(glGetProgramInfoLog(self.shader_program))
            raise RuntimeError("Shader program linking error")

        glUseProgram(self.shader_program)

    def init_particles(self):
        # Initialize particle positions and colors
        num_particles = 1000
        self.positions = np.random.uniform(-1, 1, (num_particles, 3)).astype(np.float32)
        self.colors = np.random.uniform(0, 1, (num_particles, 3)).astype(np.float32)

        self.vertex_array = glGenVertexArrays(1)
        glBindVertexArray(self.vertex_array)

        self.vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, self.positions.nbytes, self.positions, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        self.color_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.color_buffer)
        glBufferData(GL_ARRAY_BUFFER, self.colors.nbytes, self.colors, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

    def render(self):
        glUseProgram(self.shader_program)
        glBindVertexArray(self.vertex_array)
        glDrawArrays(GL_POINTS, 0, len(self.positions))
        pygame.display.flip()
        pygame.time.wait(10)
