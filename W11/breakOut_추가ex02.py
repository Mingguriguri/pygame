'''
[추가 ②]
- 벽돌 색상 다양하게 설정하기
- 공의 색상을 부딪힌 벽돌 색상으로 설정하기
'''

import pygame, sys
from pygame.locals import *
import random

# 색상 상수
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def gameInit():
	global gameStart
	gameStart = False
	stick.centerx = width / 2
	ball.centerx = stick.centerx
	ball.bottom = stick.top

pygame.init()

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

stick = pygame.Rect(340, 470, 120, 20)

ball = pygame.Rect(390, 240, 20, 20)
vel = [-1, 1]
ballColor = RED	# [추가] 공 색깔변수

brickList = []
x = 20
y = 10

for i in range(5):
	for j in range(9):
		# [변경] 각 벽돌을 딕셔너리 형태로 생성
		brick = {'rect': pygame.Rect(x, y, 80, 30),
				 'color': random.choice([RED, GREEN, BLUE, WHITE])}
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
		if ball.colliderect(brick['rect']):	# 변경
			ballColor = brick['color']	# [추가] 공 색상을 부딪힌 벽돌 색상으로 설정
			brickList.remove(brick)
			vel[1] *= -1
			count += 1

	screen.fill((0, 0, 0))
	if not gameStart:
		text = font.render('Press SPACE KEY to Start', True, (255, 255, 255))
		screen.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
	else:
		text = font.render('SCORE: %d' % count, True, (255, 255, 255))
		screen.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))

	for brick in brickList:
		pygame.draw.rect(screen, brick['color'], brick['rect'])	# 변경

	pygame.draw.rect(screen, (255, 255, 255), stick)
	pygame.draw.rect(screen, ballColor, ball)	# 변경
	pygame.display.update()