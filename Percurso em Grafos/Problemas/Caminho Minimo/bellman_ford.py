import sys
sys.path.append('../../')
from graphs import *

def bellman_ford(graph: Graph, src: int):
	total_v = graph.get_total_v();
	distance = [infinity] * total_v;
	graph_matrix = graph.get_matrix()

	distance[0] = 0;

	for i in range(total_v - 1):
		has_update = False

		for j in range(total_v):
			total_adj = graph.get_adj_list(j)
			
			for k in range(len(total_adj)):
				if distance[j] + graph_matrix[j][total_adj[k]] < distance[total_adj[k]] :
					distance[total_adj[k]] = distance[j] + graph_matrix[j][total_adj[k]]
					has_update = True

		if has_update == False:
			break

	return distance

	

inf = infinity
graph = Graph([[ 0 , 10,inf,inf,inf, 8 ],
			   [inf, 0 ,inf, 2 ,inf,inf],
			   [inf, 1 , 0 ,inf,inf,inf],
			   [inf,inf, -2, 0 ,inf,inf],
			   [inf, -4,inf, -1, 0 ,inf],
			   [inf,inf,inf,inf, 1 , 0 ]])

print(bellman_ford(graph,0))
