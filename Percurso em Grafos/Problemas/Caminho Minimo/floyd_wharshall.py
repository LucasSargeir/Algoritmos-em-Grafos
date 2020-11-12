import sys
sys.path.append('../../')
from graphs import *

def floyd_wharshall(graph: Graph):
	total_v = graph.get_total_v()
	distance = graph.get_matrix()
	
	for i in range(total_v):
		for j in range(total_v):
			for k in range(total_v):
				if distance[j][i] + distance[i][k] < distance[j][k]:
					distance[j][k] = distance[j][i] + distance[i][k]

	return distance

inf = infinity
graph = Graph([[ 0 ,inf, -2,inf],
			   [ 4 , 0 , 3 ,inf],
			   [inf,inf, 0 , 2 ],
			   [inf, -1,inf, 0 ]])

print_m(floyd_wharshall(graph))
