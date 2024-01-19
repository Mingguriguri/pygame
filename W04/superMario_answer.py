import pygame, sys
from pygame.locals import *
import random

width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))

bgImage = pygame.image.load('background.png')
bgImage = pygame.transform.scale(bgImage, (width, height))

r1 = pygame.Rect(width/2-30, 410, 60, 100)
mario1 = pygame.image.load('mario.png')
mario1 = pygame.transform.scale(mario1, (r1.w, r1.h))
mario2 = pygame.transform.flip(mario1, True, False)
image1 = mario1

coins = []
for i in range(30):
	coin = pygame.Rect(random.randint(0, width-40), random.randint(0,470), 40, 40)
	coins.append(coin)
image2 = pygame.image.load('coin.png')
image2 = pygame.transform.scale(image2, (40,40))

pygame.mixer.music.load('bgm.ogg')
pygame.mixer.music.play(-1, 0)


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 주인공 움직임
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r1.left >= 0:
		r1.left -= 5
		image1 = mario1
	elif keyInput[K_RIGHT] and r1.right <= width:
		r1.right += 5
		image1 = mario2
	elif keyInput[K_UP] and r1.top >= 0:
		r1.top -= 5
	elif keyInput[K_DOWN] and r1.bottom <= height:
		r1.bottom += 5


	# 충돌 감지
	for coin in coins:
		if r1.colliderect(coin):
			coins.remove(coin)

	screen.blit(bgImage, screen.get_rect())
	for coin in coins:
		screen.blit(image2, coin)
	screen.blit(image1, r1)
	pygame.display.update()