import pygame, sys
from pygame.locals import *

pygame.init()

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

stick = pygame.Rect(340, 470, 120, 20)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 막대기의 움직임(좌우)
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and stick.left >= 0:
		stick.left -= 1
	elif keyInput[K_RIGHT] and stick.right <= width:
		stick.right += 1

	screen.fill((0, 0, 0))
	pygame.draw.rect(screen, (255, 255, 255), stick)
	pygame.display.update()