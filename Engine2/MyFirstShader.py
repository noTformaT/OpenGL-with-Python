from glapp.PyOGLApp import *
from glapp.GraphicsData import *
import numpy as np
from glapp.Utils import *
from glapp.Square import *

vertex_shader = r'''
#version 330

in vec3 position;
in vec3 vertex_color;
out vec3 color;

void main()
{
    gl_Position = vec4(position.x, position.y, position.z, 1);
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core

in vec3 color;

out vec4 frag_color;

void main()
{
    frag_color = vec4(color, 1);
}
'''

class MyFirstShader(PyOGLApp):
    def __init__(self) -> None:
        super().__init__(0, 0, 1000, 800)
        self.square = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id)
        

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.square.draw()

MyFirstShader().mainLoop()