from pygame.locals import *
from .Camera import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *

class PyOGLApp:
    def __init__(self, screenPosx, screenPosY, screen_width, screen_height) -> None:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screenPosx, screenPosY)

        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()

        screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('OpenGL in Python')
        self.camera = Camera()

    def draw_world_axes(self):
        glLineWidth(0.1)
        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3f(-1000, 0, 0)
        glVertex3f(1000, 0, 0)

        glColor3f(0, 1, 0)
        glVertex3f(0, -1000, 0)
        glVertex3f(0, 1000, 0)

        glColor3f(0, 0, 1)
        glVertex3f(0, 0, -1000)
        glVertex3f(0, 0, 1000)

        glEnd()

        sphere = gluNewQuadric()

        glColor3f(1, 0, 0)
        glPushMatrix()
        glTranslatef(1, 0, 0)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()


        glColor3f(0, 1, 0)
        glPushMatrix()
        glTranslatef(0, 1, 0)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        glColor3f(0, 0, 1)
        glPushMatrix()
        glTranslatef(0, 0, 1)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        glLineWidth(1.0)
        glColor3f(1, 1, 1)
    
    def initialize(self):
        pass

    def display(self):
        pass

    def camera_init(self):
        pass

    def mainLoop(self):
        done = False
        self.initialise()
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
            pygame.time.wait(16)
        pygame.quit()