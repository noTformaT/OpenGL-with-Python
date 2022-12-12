import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("OpenGL in Python")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

def draw_point(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
       
    glVertex2i(x, y)
    
    glEnd()

done = False

init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_point(231, 151, 20)
    draw_point(257, 253, 20)
    draw_point(303, 180, 15)
    draw_point(443, 228, 20)
    draw_point(435, 287, 10)
    draw_point(385, 315, 20)
    draw_point(371, 343, 10)
    draw_point(397, 377, 10)
    draw_point(435, 373, 10)

    pygame.display.flip()
    pygame.time.wait(16)

pygame.quit()