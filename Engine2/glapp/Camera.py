import pygame
from OpenGL.GLU import *
from math import *

class Camera:
    def __init__(self, init_pos=pygame.math.Vector3(0, 0, 0)) -> None:
        self.eye = init_pos
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward
        self.yaw = -45
        self.pitch = -45
        self.last_mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        self.first_mouse = True
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.008

    def rotate(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch

        if self.pitch > 89.0:
            self.pitch = 89.0

        if self.pitch < -89.0:
            self.pitch = -89.0

        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.pitch))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward = self.forward.normalize()
        self.right = self.forward.cross(pygame.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def update(self, w, h):
        if pygame.mouse.get_visible():
            return

        #mouse
        if self.first_mouse:
            self.last_mouse = pygame.mouse.get_pos()
            self.first_mouse = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(w/2, h/2)
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(-mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        #keys
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.eye -= self.forward * self.key_sensitivity
        if (keys[pygame.K_UP] or keys[pygame.K_w]):
            self.eye += self.forward * self.key_sensitivity
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.eye += self.right * self.key_sensitivity
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.eye -= self.right * self.key_sensitivity
        if (keys[pygame.K_q]):
            self.eye -= pygame.math.Vector3(0, 1, 0) * self.key_sensitivity
        if (keys[pygame.K_e]):
            self.eye += pygame.math.Vector3(0, 1, 0) * self.key_sensitivity

        self.look = self.eye + self.forward
        #print(self.look)
        gluLookAt(
            self.eye.x, self.eye.y, self.eye.z,
            self.look.x, self.look.y, self.look.z,
            self.up.x, self.up.y, self.up.z
        )