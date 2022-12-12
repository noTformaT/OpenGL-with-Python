from OpenGL.GL import *
from Mesh import *
import pygame

class LoadMesh(Mesh):
    def __init__(self, file_name, draw_type, position=pygame.Vector3(0, 0, 0), rotation=Rotation(0, pygame.Vector3(0, 1, 0)), scale=pygame.Vector3(1, 1, 1)) -> None:
        self.file_name = file_name
        vertices, triangles = self.load_drawing()
        super().__init__(vertices, triangles, draw_type, position, rotation, scale)

    def load_drawing(self):
        vertices = []
        triangles = []
        with open(self.file_name) as fp:
            line = fp.readline()
            while line:
                line = fp.readline()
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)

        return vertices, triangles