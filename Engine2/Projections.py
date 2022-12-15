from glapp.PyOGLApp import *
from glapp.GraphicsData import *
import numpy as np
from glapp.Utils import *
from glapp.Square import *
from glapp.Triangle import *
from glapp.Axes import *
from glapp.Cube import *
from glapp.LoadMesh import *

vertex_shader = r'''
#version 330

in vec3 position;
in vec3 vertex_color;

out vec3 color;

uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;

void main()
{
    gl_Position = projection_mat * inverse(view_mat)  * model_mat * vec4(position, 1);
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

class Projections(PyOGLApp):
    def __init__(self) -> None:
        super().__init__(0, 0, 700, 700)
        self.axes = None
        self.square = None
        self.triangle = None
        self.cube = None
        self.teapot = None
        self.monkey = None
        self.crah = None
        self.cortex = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(0, -1, -1))
        self.triangle = Triangle(self.program_id, pygame.Vector3(0, 0, 0))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        self.axes = Axes(self.program_id)
        self.cube = Cube(self.program_id, pygame.Vector3(0, -2, 0))
        self.teapot = LoadMesh("Resources/teapot.obj", self.program_id, 
            location=pygame.Vector3(2, 0, 0),
            scale=pygame.Vector3(1,1,1), 
            rotation=Rotation(0, pygame.Vector3(0, 1, 0)))
        self.monkey = LoadMesh("Resources/monkey_hd.obj", self.program_id, location=pygame.Vector3(4, 1.5, 0))
        self.crash = LoadMesh("Resources/crash.obj", self.program_id, location=pygame.Vector3(-4, 0.0, 0))
        self.cortex = LoadMesh("Resources/cortex.obj", self.program_id, location=pygame.Vector3(0, 4.5, 0))
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        
        self.teapot.update()
        
        #self.square.draw()
        #self.triangle.draw()
        self.axes.draw()
        #self.cube.draw()
        self.teapot.draw()
        #self.monkey.draw()
        #self.crash.draw()
        #self.cortex.draw()

Projections().mainLoop()