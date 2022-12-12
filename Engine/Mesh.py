from OpenGL.GL import *
import pygame

class Rotation:
    def __init__(self, angle, axis) -> None:
        self.angle = angle
        self.axis = axis

class Mesh:
    def __init__(self, vertices, triangles, draw_type, translation, rotaion) -> None:
        self.vertices  = vertices
        self.triangles = triangles
        self.draw_type = draw_type
        self.transtation = translation
        self.rotation = rotaion
    
    def draw(self, move=pygame.Vector3(0, 0, 0)):
        glPushMatrix()
        glTranslatef(move.x, move.y, move.z)
        glTranslatef(self.transtation.x, self.transtation.y, self.transtation.z) 
        glRotatef(self.rotation.angle, self.rotation.axis.x, self.rotation.axis.y, self.rotation.axis.z)
        for t in range(0, len(self.triangles), 3):
            glLineWidth(1)
            glColor3f(1, 1, 1)
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
            t += 3
        glPopMatrix()