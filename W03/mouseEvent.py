import pygame, sys
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((500,500))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill((209, 178, 255))
    pygame.display.update()

