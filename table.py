import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Hello Pygame")

screen.fill((255, 255, 255))

fields = {}

for i in range(11):
	k = i
	pygame.draw.polygon(screen, (0, 0, 0), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]], 5)
	#pygame.draw.circle(screen, (0, 0, 0), [50 + 32*k, 94 + 64*i], 32, 5)
	fields.update({(50 + 32*k, 94 + 64*i):True})

	for j in range(1, 11):
		pygame.draw.polygon(screen, (0, 0, 0), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]], 5)
		#pygame.draw.circle(screen, (0, 0, 0), [50 + 64*j + 32*k, 94 + 64*i], 32, 5)
		fields.update({(50 + 64*j + 32*k, 94 + 64*i):True})

mouse = pygame.mouse.get_pos()
pos = list(fields.keys())
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if ((mouse[0] - pos[0][0])**2 + (mouse[1] - pos[0][1])**2)**(1/2) < 32:
				pygame.draw.polygon(screen, (0, 0, 255), [[50 + 32*0, 50 + 64*0], [18 + 32*0, 74 + 64*0], [18 + 32*0, 114 + 64*0], [50 + 32*0, 138 + 64*0], [82 + 32*0, 114 + 64*0], [82 + 32*0, 74 + 64*0]])
				pygame.quit()

				pygame.display.update()

			pygame.display.update()

		pygame.display.update()

	pygame.display.update()