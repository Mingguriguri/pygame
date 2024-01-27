import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont(pygame.font.get_default_font(), 45)
text = font.render("Daddy's lab", False, (255,255,255))


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((0, 0, 0))
	screen.blit(text, ((width-text.get_width())/2, (height-text.get_height())/2))
	pygame.display.update()