import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *
from Camera import *

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

cube = Cube(position=pygame.Vector3(0, -1, 0))
mesh = LoadMesh("Resources/cone.obj", GL_LINE_LOOP, position=pygame.Vector3(0, 0, 0))
camera = Camera()

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

def camera_init():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update(screen.get_width(), screen.get_height())

def draw_world_axes():
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

    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    draw_world_axes()
    mesh.draw()
    cube.draw()

done = False
initialise()
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
    display()
    pygame.display.flip()
    pygame.time.wait(16)
pygame.quit()