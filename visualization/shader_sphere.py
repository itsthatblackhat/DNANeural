import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import ctypes

vertex_shader_code = """
#version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec3 color;
out vec3 fragColor;
out vec3 fragNormal;
void main() {
    fragColor = color;
    fragNormal = normal;
    gl_Position = vec4(position, 1.0);
}
"""

fragment_shader_code = """
#version 330 core
in vec3 fragColor;
in vec3 fragNormal;
out vec4 color;
void main() {
    vec3 lightDir = normalize(vec3(0.0, 0.0, 1.0));
    float diff = max(dot(fragNormal, lightDir), 0.0);
    color = vec4(fragColor * diff, 1.0);
}
"""

def generate_sphere(radius, slices, stacks):
    vertices = []
    normals = []
    colors = []
    for i in range(slices):
        lat0 = np.pi * (-0.5 + float(i) / slices)
        z0 = radius * np.sin(lat0)
        zr0 = radius * np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(i + 1) / slices)
        z1 = radius * np.sin(lat1)
        zr1 = radius * np.cos(lat1)

        for j in range(stacks + 1):
            lng = 2 * np.pi * float(j) / stacks
            x = np.cos(lng)
            y = np.sin(lng)
            vertices.append([x * zr0, y * zr0, z0])
            normals.append([x * zr0, y * zr0, z0])
            colors.append([1.0, 0.0, 0.0])
            vertices.append([x * zr1, y * zr1, z1])
            normals.append([x * zr1, y * zr1, z1])
            colors.append([0.0, 1.0, 0.0])

    vertices = np.array(vertices, dtype=np.float32)
    normals = np.array(normals, dtype=np.float32)
    colors = np.array(colors, dtype=np.float32)
    return vertices, normals, colors

class ShaderSphereRenderer:
    def __init__(self):
        self.init_shaders()
        self.init_sphere()

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

    def init_sphere(self):
        vertices, normals, colors = generate_sphere(1, 40, 40)
        self.vertex_array = glGenVertexArrays(1)
        self.vertex_buffer = glGenBuffers(1)
        self.normal_buffer = glGenBuffers(1)
        self.color_buffer = glGenBuffers(1)

        glBindVertexArray(self.vertex_array)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, self.normal_buffer)
        glBufferData(GL_ARRAY_BUFFER, normals.nbytes, normals, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.color_buffer)
        glBufferData(GL_ARRAY_BUFFER, colors.nbytes, colors, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(2)

    def render(self):
        glUseProgram(self.shader_program)
        glBindVertexArray(self.vertex_array)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, len(generate_sphere(1, 40, 40)[0]))
        pygame.display.flip()
        pygame.time.wait(10)
