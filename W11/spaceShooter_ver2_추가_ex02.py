'''
[추가 ②]
- 특정 아이템과 부딪히면 hp 증가하기
'''

import pygame, sys
from pygame.locals import *
import random

def drawEnemies():
	for enemy in enemies:
		enemy['rect'].x -= 3
		screen.blit(enemy['image'], enemy['rect'])
		if enemy['rect'].left < 0:
			enemies.remove(enemy)

# [추가] 아이템 그리기
def drawItems():
	for item in items:
		item['rect'].x -= 5
		screen.blit(item['image'], item['rect'])
		if item['rect'].left < 0:
			items.remove(item)

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

bgImage = pygame.image.load('background.jpg')
bgImage = pygame.transform.scale(bgImage, (width, height))
backX = 0
backX2 = width-10

img = pygame.image.load('spaceship.png')
spaceship = {'rect': pygame.Rect(30, 215, 70, 70),
			 'image': pygame.transform.scale(img, (70, 70))}

bullets = []
bulletImage = pygame.image.load('bullet1.png')
bulletImage = pygame.transform.scale(bulletImage, (20, 10))

enemies = []
cnt = 0
imgList = [pygame.image.load('stone1.png'),
		   pygame.image.load('stone2.png')]

score = 0
font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
text = font.render(str(score), True, (255, 255, 255))

hpBar = pygame.Rect(10, 10, 200, 20)
outline = pygame.Rect(10, 10, 200, 20)

# [추가] 아이템 이미지
items = []
itemCnt = 0
hpImage = pygame.image.load('hp.png')
hpImage = pygame.transform.scale(hpImage, (30, 30))

while True:
	cnt += 1
	itemCnt += 1
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			bullet = pygame.Rect(spaceship['rect'].centerx - 10,
								 spaceship['rect'].centery - 5,
								 20, 10)
			bullets.append(bullet)

	keyInput = pygame.key.get_pressed()
	if keyInput[K_RIGHT]:
		backX -= 3
		backX2 -= 3
		drawEnemies()
		drawItems()	# 함수 호출

	if keyInput[K_UP] and spaceship['rect'].top > 0:
		spaceship['rect'].top -= 3
	elif keyInput[K_DOWN] and spaceship['rect'].bottom < height:
		spaceship['rect'].bottom += 3

	if cnt == 30:
		cnt = 0
		size = random.randint(5, 30)
		enemy = {'rect': pygame.Rect(width, random.randint(0, height-size),
									 size, size),
				 'image': pygame.transform.scale(random.choice(imgList), (size, size))}
		enemies.append(enemy)

	# [추가] 타이밍에 맞게 아이템 추가하기
	if itemCnt == 150:
		itemCnt = 0
		item = {'rect': pygame.Rect(width, random.randint(0, height-30),
									 30, 30),
				 'image': hpImage}
		items.append(item)

	for bullet in bullets:
		for enemy in enemies:
			if bullet.colliderect(enemy['rect']):
				enemies.remove(enemy)
				score += 1
				text = font.render(str(score), True, (255, 255, 255))

	for enemy in enemies:
		if spaceship['rect'].colliderect(enemy['rect']):
			enemies.remove(enemy)
			hpBar.width -= 10
			if hpBar.width <= 0:
				pygame.quit()
				sys.exit()

	# [추가] 주인공과 아이템의 충돌감지
	for item in items:
		if spaceship['rect'].colliderect(item['rect']):
			items.remove(item)
			if hpBar.width <= 190:
				hpBar.width += 10

	if backX <= width * -1:
		backX = width-10

	if backX2 <= width * -1:
		backX2 = width-10

	if backX >= 0:
		backX -= width-10
		backX2 -= width-10

	screen.blit(bgImage, (backX, 0))
	screen.blit(bgImage, (backX2, 0))
	drawEnemies()
	drawItems()	# 함수 호출

	for bullet in bullets:
		bullet.x += 5
		screen.blit(bulletImage, bullet)
		if bullet.right >= width:
			bullets.remove(bullet)

	screen.blit(spaceship['image'], spaceship['rect'])
	screen.blit(text, ((width - text.get_width()) / 2, 10))

	pygame.draw.rect(screen, (255, 0, 0), hpBar)
	pygame.draw.rect(screen, (255, 255, 255), outline, 2)
	pygame.display.update()