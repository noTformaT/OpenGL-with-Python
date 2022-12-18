from pygame.locals import *
from .Camera import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *

class PyOGLApp:
    def __init__(self, screenPosx, screenPosY, screen_width, screen_height) -> None:
        #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screenPosx, screenPosY)

        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()

        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)

        self.screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('Кеп єбаше магію')
        self.camera = None
        self.program_id = None
        self.clock = pygame.time.Clock()
    
    def initialize(self):
        pass

    def display(self):
        pass

    def camera_init(self):
        pass

    def mainLoop(self):
        done = False
        self.initialize()
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        done = True
                        pygame.event.set_grab(False)
                        pygame.mouse.set_visible(True)
            self.camera_init()
            self.display()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()