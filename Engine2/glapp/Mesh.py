from OpenGL.GL import *
import pygame
from .GraphicsData import *
import numpy as np
from .Uniform import *
from .Transformations import *

class Mesh:
    def __init__(self, program_id, vertices, vertex_colors, draw_type, 
        translation=pygame.Vector3(0, 0, 0),
        rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
        sc=pygame.Vector3(1, 1, 1)) -> None:
        self.program_id = program_id
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        
        position = GraphicsData("vec3", self.vertices)
        position.create_variable(program_id, "position")

        colors = GraphicsData("vec3", vertex_colors)
        colors.create_variable(program_id, "vertex_color")

        self.transfomation_mat = identity_mat()
        self.transfomation_mat = rotate(self.transfomation_mat, rotation.angle, "Y")
        self.transfomation_mat = translate(self.transfomation_mat, translation.x, translation.y, translation.z)
        self.transfomation_mat = scale3(self.transfomation_mat, sc.x, sc.y, sc.z)
        
        self.transfomation = Uniform("mat4", self.transfomation_mat)
        self.transfomation.find_variable(program_id, "model_mat")

    def add_rotation(self):
        self.transfomation_mat = rotateA(self.transfomation_mat, 3, pygame.Vector3(0, 1, 0))
        self.transfomation.update_data(self.transfomation_mat)


    def draw(self):
        self.transfomation.load()
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))

    def update(self, dt=0.016):
        self.add_rotation()