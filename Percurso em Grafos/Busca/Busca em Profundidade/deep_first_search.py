import sys
sys.path.append('../../')
from graphs import *

def DFS_pre_ordering(graph: Graph, src: int):
	def sequence(graph: Graph, src: int, visited: list):
		visited[src] = True
		print(str(src + 1) +' ', end = '')
		for i in graph.get_adj_list(src):
			if visited[i] == False:
				sequence(graph, i, visited)

	print('Pré Ordem: { ', end = '')
	sequence(graph, src, [False] * graph.get_total_v())
	print('}')

def DFS_post_ordering(graph: Graph, src: int):
	def sequence(graph: Graph, src: int, visited: list):
		visited[src] = True
		for i in graph.get_adj_list(src):
			if visited[i] == False:
				sequence(graph, i, visited)
		print(str(src + 1) + ' ', end = '')

	print('Pós Ordem: { ', end = '')
	sequence(graph, src, [False] * graph.get_total_v())
	print('}')


inf = infinity
graph = Graph([[ 0 , 1 ,inf,inf, 1 ],
			   [ 1 , 0 , 1 ,inf, 1 ],
			   [inf, 1 , 0 ,inf,inf],
			   [inf,inf,inf, 0 , 1 ],
			   [ 1 , 1 ,inf, 1 , 0 ]])

DFS_pre_ordering(graph, 1)
DFS_post_ordering(graph, 1)