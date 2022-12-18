from OpenGL.GL import *
import pygame
from .GraphicsData import *
import numpy as np
from .Uniform import *
from .Transformations import *
from .Texture import *
from .Material import *

class Mesh:
    def __init__(self,
            vertices = None, 
            v_normals = None, 
            v_uvs = None, 
            vertex_colors = None, 
            draw_type = GL_TRIANGLES, 
            image_name=None, 
            translation=pygame.Vector3(0, 0, 0),
            rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
            sc=pygame.Vector3(1, 1, 1),
            material=None
        ) -> None:

        self.material = material
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        
        position = GraphicsData("vec3", self.vertices)
        position.create_variable(material.program_id, "position")

        if v_normals is not None:
            normals = GraphicsData("vec3", v_normals)
            normals.create_variable(material.program_id, "vertex_normal")

        colors = GraphicsData("vec3", vertex_colors)
        colors.create_variable(material.program_id, "vertex_color")

        if v_uvs is not None:
            uv = GraphicsData("vec2", v_uvs)
            uv.create_variable(material.program_id, "vertex_uv")

        self.transfomation_mat = identity_mat()
        self.transfomation_mat = rotateA(self.transfomation_mat, rotation.angle, rotation.axis)
        self.transfomation_mat = translate(self.transfomation_mat, translation.x, translation.y, translation.z)
        self.transfomation_mat = scale3(self.transfomation_mat, sc.x, sc.y, sc.z)

        self.transfomation = Uniform("mat4", self.transfomation_mat)
        self.transfomation.find_variable(material.program_id, "model_mat")

        self.image = Texture(image_name)
        self.texture = Uniform("sampler2D", [self.image.texture_id, 1])
        self.texture.find_variable(material.program_id, "tex")

    def add_rotation(self):
        self.transfomation_mat = rotateA(self.transfomation_mat, 3, pygame.Vector3(0, 1, 0))
        self.transfomation.update_data(self.transfomation_mat)


    def draw(self, camera, light):
        self.material.use()

        camera.update(self.material.program_id)
        light.update(self.material.program_id)

        self.texture.load()
        self.transfomation.load()
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))

    def update(self, dt=0.016):
        self.add_rotation()