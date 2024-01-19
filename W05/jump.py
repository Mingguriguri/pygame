import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 400
screen = pygame.display.set_mode((width, height))

bgImage = pygame.image.load('background.jpg')
bgImage = pygame.transform.scale(bgImage, (width, height))

r1 = pygame.Rect(0, 223, 50, 80)

image1 = pygame.image.load('walk.png')
image1 = pygame.transform.scale(image1, (50, 80))
image2 = pygame.image.load('jump.png')
image2 = pygame.transform.scale(image2, (50, 80))
bear = image1

while True:
	pygame.time.delay(1)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r1.left >= 0:
		r1.left -= 1
	if keyInput[K_RIGHT] and r1.right <= width:
		r1.right += 1

	# 점프기능

	screen.blit(bgImage, (0, 0))	# 배경이미지
	screen.blit(bear, r1)
	pygame.display.update()