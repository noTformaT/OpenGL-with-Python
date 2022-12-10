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

ortho_left = 0
ortho_right = 4
ortho_top = -1
ortho_bottom = 1

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("OpenGL in Python")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

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

def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
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
            line.append( [map_value(0, screen_width, ortho_left, ortho_right, p[0]),  map_value(0, screen_height, ortho_bottom, ortho_top, p[1]) ])

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_lines()
    plot_graph()

    pygame.display.flip()
    pygame.time.wait(16)

pygame.quit()