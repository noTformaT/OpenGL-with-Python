from glapp.PyOGLApp import *
from glapp.GraphicsData import *
import numpy as np
from glapp.Utils import *
from glapp.Square import *
from glapp.Triangle import *

vertex_shader = r'''
#version 330

in vec3 position;
in vec3 vertex_color;

out vec3 color;

uniform vec3 translation;

void main()
{
    vec3 pos = position + translation;
    gl_Position = vec4(pos, 1);
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
        super().__init__(0, 0, 700, 700)
        self.square = None
        self.triangle = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-1, 0, 0))
        self.triangle = Triangle(self.program_id, pygame.Vector3(0, 0, 0))
        

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.square.draw()
        self.triangle.draw()

MyFirstShader().mainLoop()