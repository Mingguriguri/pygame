import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

# 배경
bgImage = pygame.image.load('test.png')
bgImage = pygame.transform.scale(bgImage, (width, height))
backX = 0 # 좌표 A의 초기값
backX2 = width # 좌표 B의 초기값

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(bgImage, (backX, 0))
	screen.blit(bgImage, (backX2, 0))

	pygame.display.update()