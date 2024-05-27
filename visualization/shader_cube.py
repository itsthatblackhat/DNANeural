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

def generate_cube():
    vertices = [
        -1, -1, -1, 1.0, 0.0, 0.0,
         1, -1, -1, 0.0, 1.0, 0.0,
         1,  1, -1, 0.0, 0.0, 1.0,
        -1,  1, -1, 1.0, 1.0, 0.0,
        -1, -1,  1, 1.0, 0.0, 1.0,
         1, -1,  1, 0.0, 1.0, 1.0,
         1,  1,  1, 1.0, 0.5, 0.5,
        -1,  1,  1, 0.5, 0.5, 1.0
    ]
    indices = [
        0, 1, 2, 2, 3, 0,
        4, 5, 6, 6, 7, 4,
        0, 1, 5, 5, 4, 0,
        2, 3, 7, 7, 6, 2,
        0, 3, 7, 7, 4, 0,
        1, 2, 6, 6, 5, 1
    ]
    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)

class ShaderCubeRenderer:
    def __init__(self):
        self.init_shaders()
        self.init_cube()

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

    def init_cube(self):
        vertices, indices = generate_cube()
        self.vertex_array = glGenVertexArrays(1)
        self.vertex_buffer = glGenBuffers(1)
        self.index_buffer = glGenBuffers(1)

        glBindVertexArray(self.vertex_array)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(3 * vertices.itemsize))
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.index_buffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    def render(self):
        glUseProgram(self.shader_program)
        glBindVertexArray(self.vertex_array)
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)
