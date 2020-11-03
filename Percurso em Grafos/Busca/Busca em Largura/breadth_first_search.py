import sys
sys.path.append('../../')
from graphs import *

def BFS(graph: Graph, src: int):
	visited = [False] * graph.get_total_v()
	queue = []
	queue.append(src)

	print('Ordem por nível: { ', end = '')

	while len(queue) != 0:
		src = queue.pop(0)
		if visited[src] == False:
			print(str(src + 1) + ' ', end = '')
			visited[src] = True
			for i in graph.get_adj_list(src):
				if visited[i] == False:
					queue.append(i)
	print('}')

inf = infinity
graph = Graph([[ 0 , 1 ,inf,inf, 1 ],
			   [ 1 , 0 , 1 ,inf, 1 ],
			   [inf, 1 ,0 ,inf,inf],
			   [inf,inf,inf, 0 , 1 ],
			   [ 1 , 1 ,inf, 1 , 0 ]])

BFS(graph, 1)