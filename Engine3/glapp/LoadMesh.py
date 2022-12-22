from OpenGL.GL import *
from .Mesh import *
import pygame
import random
from .Utils import *
from .Transformations import *


class LoadMesh(Mesh):
    def __init__(self, 
                file_name=None, 
                image_name="Resources/uv.png", 
                draw_type=GL_TRIANGLES, 
                location=pygame.Vector3(0, 0, 0),
                rotation=Rotation(0, pygame.Vector3(0, 1, 0)), 
                scale=pygame.Vector3(1, 1, 1),
                material=None,
                world_cubemap=None
        ) -> None:
        coordinates, triangles, uvs, uvs_ind, normals, normal_ind = self.load_drawing(file_name)
        
        vertices = format_vertices(coordinates, triangles)
        vertex_normal = format_vertices(normals, normal_ind)
        vertex_uv = format_vertices(uvs, uvs_ind)
        
        colors = []
        for i in range(len(vertices)):
            c = []
            #c.append(random.random())
            #c.append(random.random())
            #c.append(random.random())
            colors.append([1, 1, 1])
            
        super().__init__(
            vertices=vertices, 
            v_normals=vertex_normal, 
            v_uvs=vertex_uv, 
            vertex_colors=colors, 
            draw_type=draw_type,
            image_name=image_name, 
            translation=location,
            rotation=rotation,
            sc=scale,
            material=material,
            world_cube_map=world_cubemap)

    def load_drawing(self, file_name):
        vertices = []
        triangles = []
        normals = []
        normal_ind = []
        uvs = []
        uvs_ind = []
        with open(file_name) as fp:
            line = fp.readline()
            while line:
                line = fp.readline()
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                
                if line[:3] == "vt ":
                    vx, vy = [float(value) for value in line[3:].split()]
                    uvs.append((vx, vy))

                if line[:3] == "vn ":
                    vx, vy, vz = [float(value) for value in line[3:].split()]
                    normals.append((vx, vy, vz))

                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)

                    uvs_ind.append([int(value) for value in t1.split('/')][1]-1)
                    uvs_ind.append([int(value) for value in t2.split('/')][1]-1)
                    uvs_ind.append([int(value) for value in t3.split('/')][1]-1)

                    normal_ind.append([int(value) for value in t1.split('/')][2]-1)
                    normal_ind.append([int(value) for value in t2.split('/')][2]-1)
                    normal_ind.append([int(value) for value in t3.split('/')][2]-1)

        return vertices, triangles, uvs, uvs_ind, normals, normal_ind