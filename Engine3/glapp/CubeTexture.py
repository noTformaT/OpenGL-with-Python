from .Texture import *

class CubeTexture:
    def __init__(self, file_names) -> None:

        self.texture_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture_id)

        i = 0
        
        for i in range(len(file_names)):
            file_name, swap = file_names[i]
            surface = pygame.image.load(file_name)
            width = surface.get_width()
            height = surface.get_height()
            pixel_data = pygame.image.tostring(surface, "RGBA", swap)

            glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixel_data)
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glBindTexture(GL_TEXTURE_CUBE_MAP, 0)