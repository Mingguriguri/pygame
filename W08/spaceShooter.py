import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

# 배경

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	pygame.display.update()