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
        
        self.teapot = None
        self.monkey = None
        self.crah = None
        self.cortex = None

        self.light_0 = None
        self.light_1 = None

        self.lights = []

    def initialize(self):
        mat = Material("Shaders/vert_main_pass.glsl", "Shaders/frag_main_pass.glsl")
        mat_axes = Material("Shaders/vert_color_vertex.glsl", "Shaders/frag_color_vertex.glsl")

        self.camera = Camera(
            w=self.screen_width, 
            h=self.screen_height
        )

        self.axes = Axes(
            material=mat_axes
        )
       
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

        self.light_0 = Light(
            position=pygame.Vector3(-5, 5, 5),
            color=pygame.Vector3(0, 0.0, 1.0),
            light_number=0
        )
        self.lights.append(self.light_0)

        self.light_1 = Light(
            position=pygame.Vector3(5, 5, 5),
            color=pygame.Vector3(1.0, 0.843, 0),
            light_number=1)
        self.lights.append(self.light_1)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

    def camera_init(self):
        pass

    def display(self):
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        self.teapot.update()
        self.monkey.update()
        self.crash.update()
        self.cortex.update()

        self.camera.update_control()

        self.axes.draw(self.camera, self.light_0)
        
        self.teapot.draw(self.camera, self.light_0)
        self.monkey.draw(self.camera, self.light_0)
        self.crash.draw(self.camera, self.light_0)
        self.cortex.draw(self.camera, self.light_0)

Projections().mainLoop()