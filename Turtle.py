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

ortho_left = -400
ortho_right = 400
ortho_top = -300
ortho_bottom = 300

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("OpenGL in Python")

current_position = (0, 0)
direction = np.array([0, 1, 0])
draw_length = 50

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

def line_to(x, y):
    global current_position

    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x, y)
    current_position = (x, y)
    glEnd()

def rest_turtle():
    global current_position
    global direction
    current_position = (0, 0)
    direction = np.array([0, 1, 0])

def draw_turtle():
    forward()
    forward()

def forward():
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)

done = False

init_ortho()

glLineWidth(1.0)
glPointSize(1.0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()

    

    rest_turtle()
    draw_turtle()

    pygame.display.flip()
    pygame.time.wait(16)

pygame.quit()