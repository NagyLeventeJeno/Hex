import pygame
from pygame.locals import *
from collections import defaultdict
import heapq

pygame.init()

screen = pygame.display.set_mode((700, 700))

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

class Vertex:
	def __init__(self, pos):
		self.coordinates = pos
		self.parent = None
		self.distance = float('inf')

screen.fill((255, 255, 255))
color = "red"
fields = {}
values = {}
blue_graph = Graph()
red_graph = Graph()
red_start = [(0, f) for f in range(7)]
red_end = [(6, g) for g in range(7)]
blue_start = [(h, 0) for h in range(7)]
blue_end = [(d, 6) for d in range(7)]
red_won = False
blue_won = False

def update_values():
	for i in range(7):
		for j in range(7):
			if (i == 1 and j == 4) or (i == 5 and j == 2) or (i == 2 and j == 2) or (i == 4 and j == 4):
				values[(i, j)] = 0
			elif fields[(i,j)] == "blue":
				values[(i,j)] = 1000000
			elif fields[(i,j)] == "white":
				values[(i,j)] = 100
			elif fields[(i,j)] == "red":
				values[(i,j)] = 10

def get_neighbors(pos):
	i, j = pos
	potential_neighbors = [(i, j - 1), (i + 1, j -1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j)]
 
	valid_neighbors = []

	for n in potential_neighbors:
		if 0 <= n[0] <= 6 and 0 <= n[1] <= 6:
			valid_neighbors.append(n)

	return valid_neighbors

def shortest_path():
	nodes = {(i,j): Vertex((i,j)) for i in range(7) for j in range(7)}
	pq = []
	for i in range(7):
		start_nodes = (i, 3)
		if fields[start_nodes] != "blue":
			dist = values[start_nodes]
			nodes[start_nodes].distance = dist
			heapq.heappush(pq, (dist,start_nodes))
	while pq:
		dist, opt = heapq.heappop(pq)
		if dist > nodes[opt].distance:
			continue
		if opt[1] == 6:
			return reconstruct_path(nodes, opt)
		for neighbors_pos in get_neighbors(opt):
			new_distance = nodes[opt].distance + values[neighbors_pos]
			if new_distance < nodes[neighbors_pos].distance:
				nodes[neighbors_pos].distance = new_distance
				nodes[neighbors_pos].parent = opt
				heapq.heappush(pq, (new_distance, neighbors_pos))
	return None
				
def reconstruct_path(nodes, opt):
	if opt[1] == 6:
		path = []
		current_node = opt
		while current_node is not None:
			path.append(current_node)
			current_node = nodes[current_node].parent
		path.reverse()
		for step in path:
			if fields[step] == "white":
				return step

def ai_step(a, b):
	step = (a, b)
	fields[step] = "red"

	for i in range(step[0] - 1, step[0] + 2):
		for j in range(step[1] - 1, step[1] + 2):
			if 0 <= i <= 6 and 0 <= j <= 6:
				if not (i == step[0] and j == step[1]) and not (i == step[0] - 1 and j == step[1] - 1) and not (i == step[0] + 1 and j == step[1] + 1):
					if fields[(i,j)] == "red":
						red_graph.addEdge(step, (i,j))
						red_graph.addEdge((i,j), step)

for i in range(7):
	k = i

	pygame.draw.polygon(screen, (0, 0, 0), [[50 + 32*k, 50 + 64*i], [18 + 32*k, 74 + 64*i], [18 + 32*k, 114 + 64*i], [50 + 32*k, 138 + 64*i], [82 + 32*k, 114 + 64*i], [82 + 32*k, 74 + 64*i]], 5)
	pygame.draw.circle(screen, (0, 0, 0), [50 + 32*k, 94 + 64*i], 32, 5)
	fields.update({(i, 0):"white"})

	for j in range(1, 7):
		pygame.draw.polygon(screen, (0, 0, 0), [[50 + 64*j + 32*k, 50 + 64*i], [18 + 64*j + 32*k, 74 + 64*i], [18 + 64*j + 32*k, 114 + 64*i], [50 + 64*j + 32*k, 138 + 64*i], [82 + 64*j + 32*k, 114 + 64*i], [82 + 64*j + 32*k, 74 + 64*i]], 5)
		pygame.draw.circle(screen, (0, 0, 0), [50 + 64*j + 32*k, 94 + 64*i], 32, 5)
		fields.update({(i, j):"white"})

pos = list(fields.keys())

ai_step(3, 3)
color = "blue"

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			for p in pos:
				if ((mouse[0] - (50 + 64*p[1] + 32*p[0]))**2 + (mouse[1] - (94 + 64*p[0]))**2)**(1/2) <= 32:
					if fields[p] == "white":
						if color == "blue":
							fields[p] = "blue"

							for i in range(p[0] - 1, p[0] + 2):
								for j in range(p[1] - 1, p[1] + 2):
									if i >= 0 and j >= 0 and i <= 6 and j <= 6:
										if not (i == p[0] and j == p[1]) and not (i == p[0] - 1 and j == p[1] - 1) and not (i == p[0] + 1 and j == p[1] + 1):
											if fields[(i, j)] == "blue":
												blue_graph.addEdge((p[0], p[1]), (i, j))
												blue_graph.addEdge((i, j), (p[0], p[1]))

							for f in blue_start:
								visited = blue_graph.DFS(f)

								for g in blue_end:
									if g in visited:
										blue_won = True

							if blue_won:
								print("Blue won the game.")
							else:
								color = "red"

	if not blue_won and not red_won and color == "red":
		step = None
		for i in range(7):
			for j in range(7):
				if fields[(i, j)] == "red":
					if (0 <= i-1 <= 6) and (0 <= j <= 6) and fields[(i-1, j)] == "blue":
						if (0 <= i-1 <= 6) and (0 <= j+1 <= 6) and fields[(i-1, j+1)] == "white":
							step = (i-1, j+1)
					elif (0 <= i-1 <= 6) and (0 <= j+1 <= 6) and fields[(i-1, j+1)] == "blue":
						if (0 <= i-1 <= 6) and (0 <= j <= 6) and fields[(i-1, j)] == "white":
							step = (i-1, j)
					elif (0 <= i+1 <= 6) and (0 <= j <= 6) and fields[(i+1, j)] == "blue":
						if (0 <= i+1 <= 6) and (0 <= j-1 <= 6) and fields[(i+1, j-1)] == "white":
							step = (i+1, j-1)
					elif (0 <= i+1 <= 6) and (0 <= j-1 <= 6) and fields[(i+1, j-1)] == "blue":
						if (0 <= i+1 <= 6) and (0 <= j <= 6) and fields[(i+1, j)] == "white":
							step = (i+1, j)

		if step == None:
			if fields[(1, 4)] == "blue":
				if fields[(2, 2)] == "white":
					step = (2, 2)
			elif fields[(2, 2)] == "blue":
				if fields[(1, 4)] == "white":
					step = (1, 4)
			elif fields[(5, 2)] == "blue":
				if fields[(4, 4)] == "white":
					step = (4, 4)
			elif fields[(4, 4)] == "blue":
				if fields[(5, 2)] == "white":
					step = (5, 2)

		if step == None:
			if fields[(1, 4)] == "white" and fields[(2, 2)] == "white":
				step = (1, 4)
			elif fields[(5, 2)] == "white" and fields[(4, 4)] == "white":
				step = (5, 2)

		if step == None:
			update_values()
			step = shortest_path()

		if step:
			fields[step] = "red"

		for i in range(step[0] - 1, step[0] + 2):
			for j in range(step[1] - 1, step[1] + 2):
				if 0 <= i <= 6 and 0 <= j <= 6:
					if not (i == step[0] and j == step[1]) and not (i == step[0] - 1 and j == step[1] - 1) and not (i == step[0] + 1 and j == step[1] + 1):
						if fields[(i,j)] == "red":
							red_graph.addEdge(step, (i,j))
							red_graph.addEdge((i,j), step)

		for h in red_start:
			visited = red_graph.DFS(h)
			for d in red_end:
				if d in visited:
					red_won = True

		if red_won:
			print("Red won the game.")
		else:
			color = "blue"

	for i in range(7):
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