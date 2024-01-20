import pygame, sys
from pygame.locals import *

pygame.init()

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

stick = pygame.Rect(340, 470, 120, 20)
# 공
ball = pygame.Rect(390, 240, 20, 20)
vel = [-1, -1]
# 벽돌들
brickList = []
# 벽돌 리스트의 초기 좌표
x = 20
y = 10
for i in range(5):
	for j in range(9):
		brick = pygame.Rect(x, y, 80, 30)
		brickList.append(brick)
		x += 85
	y += 35
	x = 20

while True:
	pygame.time.delay(1)
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


	# 미션1
	ball.x += vel[0]
	ball.y += vel[1]

	if ball.left < 0 or ball.right > width:
		vel[0] *= -1
	if ball.top < 0 or ball.bottom > height:
		vel[1] *= -1

	screen.fill((0, 0, 0))
	pygame.draw.rect(screen, (255, 255, 255), stick)
	pygame.draw.rect(screen, (255, 0, 0), ball)

	for brick in brickList:
		pygame.draw.rect(screen, (0, 0, 255), brick)
	pygame.display.update()