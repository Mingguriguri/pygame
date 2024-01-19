import pygame, sys
from pygame.locals import *

# 색상 상수
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = BLUE

width = 500
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height))

# Rect 객체 생성
r1 = pygame.Rect(100,100,100,100)
r2 = pygame.Rect(100,300,50,100)
r3 = pygame.Rect(300,100,50,70)
r4 = pygame.Rect(300,300,100,100)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 키보드 이벤트 처리
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r3.left >= 0:
		r3.left -= 1
	elif keyInput[K_RIGHT] and r3.right <= width:
		r3.right += 1
	elif keyInput[K_UP] and r3.top >= 0:
		r3.top -= 1
	elif keyInput[K_DOWN] and r3.bottom <= height:
		r3.bottom += 1


	# 충돌감지
	if r3.colliderect(r1):
		color = RED
	elif r3.colliderect(r2):
		color = GREEN
	elif r3.colliderect(r4):
		color = BLACK

	screen.fill(WHITE)
	# 생성한 Rect 객체 그리기
	pygame.draw.rect(screen, RED, r1, 3)
	pygame.draw.rect(screen, GREEN, r2)
	pygame.draw.rect(screen, color, r3)
	pygame.draw.rect(screen, BLACK, r4, 3)

	pygame.display.update()