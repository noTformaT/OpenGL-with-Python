from glapp.PyOGLApp import *
from glapp.GraphicsData import *
import numpy as np
from glapp.Utils import *

vertex_shader = r'''
#version 330

in vec3 position;

void main()
{
    gl_Position = vec4(position.x, position.y, position.z, 1);
}
'''

fragment_shader = r'''
#version 330 core

out vec4 frag_color;

void main()
{
    frag_color = vec4(0, 1, 0, 1);
}
'''

class MyFirstShader(PyOGLApp):
    def __init__(self) -> None:
        super().__init__(0, 0, 1000, 800)
        self.vao_ref = None
        self.vertex_count = 0

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        glPointSize(10)

        position_data = [
            [   0, -0.9, 0],
            [-0.6,  0.8, 0],
            [ 0.9, -0.2, 0],
            [-0.9, -0.2, 0],
            [ 0.6, 0.8, 0]
        ]

        self.vertex_count = len(position_data)
        position_varible = GraphicsData("vec3", position_data)
        position_varible.create_variable(self.program_id, "position")

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_POINTS, 0, self.vertex_count)

MyFirstShader().mainLoop()