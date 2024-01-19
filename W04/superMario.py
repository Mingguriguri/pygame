import pygame, sys
from pygame.locals import *

width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(width/2-30, height/2-30, 60, 100)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 주인공 움직임
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r1.left >= 0:
		r1.left -= 1
	elif keyInput[K_RIGHT] and r1.right <= width:
		r1.right +=1
	elif keyInput[K_UP] and r1.top >= 0:
		r1.top -= 1
	elif keyInput[K_DOWN] and r1.bottom <= height:
		r1.bottom += 1

	screen.fill((255, 255, 255))
	pygame.draw.rect(screen, (0, 0, 0), r1)
	pygame.display.update()