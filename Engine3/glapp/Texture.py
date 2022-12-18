import pygame
from OpenGL.GL import *

class Texture():
    def __init__(self,file_name) -> None:
        self.surface = None
        self.texture_id = glGenTextures(1)

        if file_name is not None:
            self.surface = pygame.image.load(file_name)
            self.load_texture()

    def load_texture(self):
        width = self.surface.get_width()
        height = self.surface.get_height()

        pixel_data = pygame.image.tostring(self.surface, "RGBA", 1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixel_data)
        glGenerateMipmap(GL_TEXTURE_2D)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)

        glBindTexture(GL_TEXTURE_2D, 0)

    def load(self):
        glBindTexture(GL_TEXTURE_2D, self.texture_id)