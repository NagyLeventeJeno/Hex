import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Hello Pygame")

screen.fill((255, 255, 255))
color = "red"
fields = {}

for i in range(7):
	k = i

	pygame.draw.polygon(screen, (0, 0, 0), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]], 5)
	pygame.draw.circle(screen, (0, 0, 0), [50 + 32*k, 94 + 64*i], 32, 5)
	fields.update({(50 + 32*k, 94 + 64*i):"white"})

	for j in range(1, 7):
		pygame.draw.polygon(screen, (0, 0, 0), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]], 5)
		pygame.draw.circle(screen, (0, 0, 0), [50 + 64*j + 32*k, 94 + 64*i], 32, 5)
		fields.update({(50 + 64*j + 32*k, 94 + 64*i):"white"})

pos = list(fields.keys())

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			for p in pos:
				if ((mouse[0] - p[0])**2 + (mouse[1] - p[1])**2)**(1/2) <= 32:
					if fields[p] == "white":
						if color == "red":
							fields[p] = "red"
							color = "blue"
						else:
							fields[p] = "blue"
							color = "red"

	for i in range(7):
		k = i
		if fields[(50 + 32*k, 94 + 64*i)] == "blue":
			pygame.draw.polygon(screen, (0, 0, 255), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]])
		elif fields[(50 + 32*k, 94 + 64*i)] == "red":
			pygame.draw.polygon(screen, (255, 0, 0), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]])

		for j in range(1, 7):
			if fields[(50 + 64*j + 32*k, 94 + 64*i)] == "blue":
				pygame.draw.polygon(screen, (0, 0, 255), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]])
			elif fields[(50 + 64*j + 32*k, 94 + 64*i)] == "red":
				pygame.draw.polygon(screen, (255, 0, 0), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]])

	mouse = pygame.mouse.get_pos()
	pygame.display.update()
