import sys
sys.path.append('../../')
from graphs import *


def dijkstra(graph: Graph, src: int):
	graph_matrix = graph.get_matrix()
	vertices_size = graph.get_total_v()
	
	distance = [infinity] * vertices_size
	visited = [False] * vertices_size
	visiting = src
	distance[src] = 0

	for i in range(vertices_size):
		min_adj = infinity
		min_index = infinity
		adj_list = graph.get_adj_list(visiting)
		for v in adj_list:
			if graph_matrix[visiting][v] < min_adj and visited[v] == False:
					min_adj = graph_matrix[visiting][v]
					min_index = v
				
		visited[visiting] = True
		
		
		if min_index == infinity:
			if False in visited:
				visiting = visited.index(False)
				continue
			else:
				break;

		for v in adj_list:
			if graph_matrix[visiting][v] + distance[visiting] < distance[v] and visited[v] == False:
				distance[v] = distance[visiting] + graph_matrix[visiting][v]

		visiting = min_index

	return distance
	

if __name__ == "__main__":
	inf = infinity
	graph = Graph([[ 0 , 4 , 2 ,inf,inf],
				   [inf, 0 , 3 , 2 , 3 ],
				   [inf, 1 , 0 , 4 , 5 ],
				   [inf,inf,inf, 0 ,inf],
				   [inf,inf,inf, 1 , 0 ]])

	print(dijkstra(graph,0))