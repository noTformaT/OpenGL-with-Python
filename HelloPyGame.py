import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption("Hello PyGame")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        pygame.display.flip()
        pygame.time.wait(16)

pygame.quit()