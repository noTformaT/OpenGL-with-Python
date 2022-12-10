import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Unils import *

pygame.init()

screen_width = 800
screen_height = 600

ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("OpenGL in Python")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)

def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for p in l:
            glVertex2f(p[0], p[1])
        glEnd()

done = False

init_ortho()

glPointSize(5.0)

mouse_down = False

points = []
line = []
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            line = []
            points.append(line)
            mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            line.append( [map_value(0, screen_width, 0, ortho_width, p[0]),  map_value(0, screen_height, ortho_height, 0, p[1]) ])

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_lines()

    pygame.display.flip()
    pygame.time.wait(16)

pygame.quit()