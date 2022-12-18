from glapp.PyOGLApp import *
from glapp.GraphicsData import *
import numpy as np
from glapp.Utils import *
from glapp.Triangle import *
from glapp.Axes import *
from glapp.LoadMesh import *
from glapp.Light import *
from glapp.Material import *


class Projections(PyOGLApp):
    def __init__(self) -> None:
        super().__init__(0, 0, 700, 700)
        self.axes = None
        self.square = None
        self.triangle = None
        #self.cube = None
        self.teapot = None
        self.monkey = None
        self.crah = None
        self.cortex = None

        self.light_0 = None
        self.light_1 = None

    def initialize(self):
        mat = Material("Shaders/vert_main_pass.glsl", "Shaders/frag_main_pass.glsl")

        self.program_id = mat.program_id
        #self.square = Square(self.program_id, pygame.Vector3(0, -1, -1))
        #self.triangle = Triangle(self.program_id, pygame.Vector3(0, 0, 0))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        #self.axes = Axes(self.program_id)
        #self.cube = Cube(self.program_id, pygame.Vector3(0, -2, 0))
       
        self.teapot = LoadMesh(
            file_name="Resources/teapot.obj", 
            location=pygame.Vector3(0, 0, 0),
            scale=pygame.Vector3(1,1,1), 
            rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
            material=mat)
        
        self.monkey = LoadMesh(
            file_name="Resources/monkey_hd.obj",
            location=pygame.Vector3(4, 1.5, 0),
            material=mat
        )

        self.crash = LoadMesh(
            file_name="Resources/crash.obj",
            location=pygame.Vector3(-4, 0.0, 0),
            material=mat
        )

        self.cortex = LoadMesh(
            file_name="Resources/donut.obj", 
            location=pygame.Vector3(0, 4.5, 0),
            material=mat
        )

        #self.light_0 = Light(self.program_id, pygame.Vector3(5, 5, 5), pygame.Vector3(0, 0.341, 0.717), 0)
        #self.light_1 = Light(self.program_id, pygame.Vector3(-5, 5, 5), pygame.Vector3(1.0, 0.843, 0), 1)

        self.light_0 = Light(self.program_id, pygame.Vector3(-5, 5, 5), pygame.Vector3(0, 0.0, 1.0), 0)
        self.light_1 = Light(self.program_id, pygame.Vector3(5, 5, 5), pygame.Vector3(1.0, 0.843, 0), 1)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

    def camera_init(self):
        pass

    def display(self):
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()

        self.light_0.update()
        self.light_1.update()
        
        #self.teapot.update()
        #self.monkey.update()
        #self.crash.update()
        #self.cortex.update()
        
        #self.square.draw()
        #self.triangle.draw()
        #self.axes.draw()
        #self.cube.draw()
        
        self.teapot.draw()
        self.monkey.draw()
        self.crash.draw()
        self.cortex.draw()

Projections().mainLoop()