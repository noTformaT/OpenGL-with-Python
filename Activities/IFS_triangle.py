import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Unils import *

pygame.init()

screen_width = 800
screen_height = 800

ortho_left = -400
ortho_right = 400
ortho_top = 0
ortho_bottom = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("OpenGL in Python")

current_position = (0, 0)
direction = np.array([0, 1, 0])
axiom = 'X'
rules = {
    "F": "FF",
    "X": "F+[-F-XF-X][+FF][--XF[+X]][++F-X]"
}
draw_length = 5
angle = 10
stack = []
rule_number = 5
instructions = ""
points = []
x = 0
y = 0

def run_rule(run_count):
    global instructions
    instructions = axiom
    for loops in range (run_count):
        old_system = instructions
        instructions = ""
        for c in range (0, len(old_system)):
            if (old_system[c] in rules):
                instructions += rules[old_system[c]]
            else:
                instructions += old_system[c]

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

def draw_points():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def draw_turtle():
    global x
    global y
    points.append((x, y))
    r = np.random.rand()

    if r < 0.33:
        x, y = 0.5 * x + 0.00 * y + 0.0, x * 0.0 + y * 0.5 + 0.5
    elif r <   0.66:
        x, y = 0.5 * x + 0.0 * y + 0.5, x * 0.0 + y * 0.5 + 0.0
    else:
        x, y = 0.5 * x + 0.0 * y + 0.0, 0.0 * x + 0.5 * y + 0.0

def forward(draw_length):
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)

def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))

def move_to(pos):
    global current_position
    current_position = (pos[0], pos[1])

done = False

init_ortho()

glLineWidth(1.0)
glPointSize(1.0)
glColor3f(0, 1, 0)

run_rule(rule_number)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslate(-200, 100, 0)

    glScaled(550, 550, 1)

    rest_turtle()
    draw_turtle()
    draw_points()

    pygame.display.flip()
    #pygame.time.wait(16)
    pygame.time.wait(1)

pygame.quit()