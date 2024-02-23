'''
[추가 ③]
- 벽돌을 다 깼을 때, 다음 레벨로 넘어가기
- Level 2 예시: 막대기 길이 줄이기, 벽돌 개수 늘리기
'''

import pygame, sys
from pygame.locals import *

def gameInit():
	global gameStart
	gameStart = False
	stick.centerx = width / 2
	ball.centerx = stick.centerx
	ball.bottom = stick.top

# [추가] 다음 레벨을 위한 함수
def level2():
	stick.width -= 5
	x = 5
	y = 10

	for i in range(6):
		for j in range(11):
			brick = pygame.Rect(x, y, 70, 30)
			brickList.append(brick)
			x += 72
		x = 5
		y += 35

pygame.init()

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

stick = pygame.Rect(340, 470, 120, 20)

ball = pygame.Rect(390, 240, 20, 20)
vel = [-1, 1]

brickList = []
x = 20
y = 10

for i in range(5):
	for j in range(9):
		brick = pygame.Rect(x, y, 80, 30)
		brickList.append(brick)
		x += 85
	x = 20
	y += 35

font = pygame.font.SysFont(pygame.font.get_default_font(), 50)

count = 0
gameStart = False
gameInit()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			gameStart = True

	if gameStart:
		keyInput = pygame.key.get_pressed()
		if keyInput[K_LEFT] and stick.left >= 0:
			stick.left -= 1
		elif keyInput[K_RIGHT] and stick.right <= width:
			stick.right += 1

		ball.x += vel[0]
		ball.y += vel[1]

		if ball.left < 0 or ball.right > width:
			vel[0] *= -1
		if ball.top < 0:
			vel[1] *= -1
		if ball.bottom > height:
			gameInit()

	if ball.colliderect(stick):
		ball.bottom = stick.top
		vel[1] *= -1

	for brick in brickList:
		if ball.colliderect(brick):
			brickList.remove(brick)
			vel[1] *= -1
			count += 1
			# [추가] 다음 레벨로 넘어가기
			if len(brickList) == 0:
				gameInit()
				count = 0
				level2()

	screen.fill((0, 0, 0))
	if not gameStart:
		text = font.render('Press SPACE KEY to Start', True, (255, 255, 255))
		screen.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
	else:
		text = font.render('SCORE: %d' % count, True, (255, 255, 255))
		screen.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))

	for brick in brickList:
		pygame.draw.rect(screen, (0, 0, 255), brick)

	pygame.draw.rect(screen, (255, 255, 255), stick)
	pygame.draw.rect(screen, (255, 0, 0), ball)
	pygame.display.update()