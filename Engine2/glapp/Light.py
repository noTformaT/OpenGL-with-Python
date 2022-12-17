import pygame
from .Transformations import *
from .Uniform import *

class Light:
    def __init__(self, program_id, position=pygame.Vector3(0, 0, 0), color=pygame.Vector3(1, 1, 1), light_number=0) -> None:
        self.transformation = identity_mat()
        self.program_id = program_id
        self.position = position
        self.color = color

        self.light_pos_variable = "lights_data["+ str(light_number) + "].position"
        self.light_pos = Uniform("vec3", self.position);
        self.light_pos.find_variable(self.program_id, self.light_pos_variable)

        self.light_color_variable = "lights_data["+ str(light_number) + "].color"
        self.light_color = Uniform("vec3", self.color)
        self.light_color.find_variable(self.program_id, self.light_color_variable)

        



    def update(self):
        self.light_pos.load()
        self.light_color.load()