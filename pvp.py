import pygame
from pygame.locals import *
from collections import defaultdict
###
import sys 

try:
    BOARD_SIZE = int(sys.argv[1])
except (IndexError, ValueError):
    BOARD_SIZE = 7
###

pygame.init()

screen = pygame.display.set_mode((BOARD_SIZE*100, 800)) ###

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):
		visited.add(v)

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	def DFS(self, v):
		visited = set()
		self.DFSUtil(v, visited)
		return visited

screen.fill((255, 255, 255))
color = "red"
fields = {}
blue_graph = Graph()
red_graph = Graph()
red_start = [(0, f) for f in range(BOARD_SIZE)]
red_end = [(BOARD_SIZE-1, g) for g in range(BOARD_SIZE)]
blue_start = [(h, 0) for h in range(BOARD_SIZE)]
blue_end = [(d, BOARD_SIZE-1) for d in range(BOARD_SIZE)]
red_won = False
blue_won = False

for i in range(BOARD_SIZE):
	k = i

	pygame.draw.polygon(screen, (0, 0, 0), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]], 5)
	pygame.draw.circle(screen, (0, 0, 0), [50 + 32*k, 94 + 64*i], 32, 5)
	fields.update({(i, 0):"white"})

	for j in range(1, BOARD_SIZE):
		pygame.draw.polygon(screen, (0, 0, 0), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]], 5)
		pygame.draw.circle(screen, (0, 0, 0), [50 + 64*j + 32*k, 94 + 64*i], 32, 5)
		fields.update({(i, j):"white"})

pos = list(fields.keys())
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			for p in pos:
				if ((mouse[0] - (50 + 64*p[1] + 32*p[0]))**2 + (mouse[1] - (94 + 64*p[0]))**2)**(1/2) <= 32:
					if fields[p] == "white":
						if color == "red":
							fields[p] = "red"

							for i in range(p[0] - 1, p[0] + 2):
								for j in range(p[1] - 1, p[1] + 2):
									if i >= 0 and j >= 0 and i <= 6 and j <= 6:
										if not (i == p[0] and j == p[1]):
											if fields[(i, j)] == "red":
												red_graph.addEdge((p[0], p[1]), (i, j))
												red_graph.addEdge((i, j), (p[0], p[1]))

							for f in red_start:
								visited = red_graph.DFS(f)

								for g in red_end:
									if g in visited:
										red_won = True

							if red_won:
								print("Red won the game.")
								running = False
							else:
								color = "blue"
						else:
							fields[p] = "blue"

							for i in range(p[0] - 1, p[0] + 2):
								for j in range(p[1] - 1, p[1] + 2):
									if i >= 0 and j >= 0 and i <= 6 and j <= 6:
										if not (i == p[0] and j == p[1]):
											if fields[(i, j)] == "blue":
												blue_graph.addEdge((p[0], p[1]), (i, j))
												blue_graph.addEdge((i, j), (p[0], p[1]))

							for h in blue_start:
								visited = blue_graph.DFS(h)

								for d in blue_end:
									if d in visited:
										blue_won = True

							if blue_won:
								print("Blue won the game.")
								running = False
							else:
								color = "red"

	for i in range(BOARD_SIZE):
		k = i
		if fields[(i, 0)] == "blue":
			pygame.draw.polygon(screen, (0, 0, 255), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]])
		elif fields[(i, 0)] == "red":
			pygame.draw.polygon(screen, (255, 0, 0), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]])

		for j in range(1, 7):
			if fields[(i, j)] == "blue":
				pygame.draw.polygon(screen, (0, 0, 255), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]])
			elif fields[(i, j)] == "red":
				pygame.draw.polygon(screen, (255, 0, 0), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]])

	mouse = pygame.mouse.get_pos()
	pygame.display.update()

pygame.quit()
