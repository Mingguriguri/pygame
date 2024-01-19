import pygame, sys
from pygame.locals import *

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(270, 170, 60, 60)
image1 = pygame.image.load('soccerBall.png')
image1 = pygame.transform.scale(image1, (60, 60))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((83, 193, 75))
    screen.blit(image1, r1)
    pygame.display.update()