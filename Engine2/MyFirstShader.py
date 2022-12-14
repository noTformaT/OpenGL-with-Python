from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *

vertex_shader = r'''
#version 330

void main()
{
    gl_Position = vec4(0, 0, 0, 1);
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
        super().__init__(0, 0, 700, 700)
        self.vao_ref = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        glPointSize(10)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_POINTS, 0, 1)

MyFirstShader().mainLoop()