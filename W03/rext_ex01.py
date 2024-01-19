# 미션 3) Rect 객체를 하나 더 추가하여, wasd 키로 움직일 수 있도록 구현하세요.
import pygame, sys
from pygame.locals import *
import random

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(width/2-50, height/2-50, 100, 100)
image1 = pygame.image.load('dcon.png')
image1 = pygame.transform.scale(image1, (r1.w, r1.h))

r2 = pygame.Rect(150, 150, 100, 100)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 키보드 이벤트 처리
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r1.left >= 0:
		r1.left -= 1
	elif keyInput[K_RIGHT] and r1.right <= width:
		r1.right += 1
	elif keyInput[K_UP] and r1.top >= 0:
		r1.top -= 1
	elif keyInput[K_DOWN] and r1.bottom <= height:
		r1.bottom += 1
	elif keyInput[K_SPACE]:
		r1.x = random.randint(0, height-r1.height)
		r1.y = random.randint(0, width-r1.width)

	# r2의 움직임 구현(wasd 키)
	if keyInput[K_a] and r2.left >= 0:
		r2.left -= 1
	elif keyInput[K_d] and r2.right <= width:
		r2.right += 1
	elif keyInput[K_w] and r2.top >= 0:
		r2.top -= 1
	elif keyInput[K_s] and r2.bottom <= height:
		r2.bottom += 1

	screen.fill((0, 0, 0))
	screen.blit(image1, r1)
	pygame.draw.rect(screen, (255, 255, 255), r2)
	pygame.display.update()
