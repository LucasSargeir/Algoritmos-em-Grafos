import sys
sys.path.append('../../')
from graphs import *
from bellman_ford import bellman_ford
from dijkstra import dijkstra


def johnson(graph: Graph, type: str = 'copy'):
	def transform_vertices(graph_matrix: list, distance: list):
		for i in range(len(graph_matrix)):
			for j in range(len(graph_matrix[i])):
					graph_matrix[i][j] += distance[i] - distance[j]

	def rollback_vertices(graph_matrix: list, distance: list):
		for i in range(len(graph_matrix)):
			for j in range(len(graph_matrix[i])):
				graph_matrix[i][j] += -distance[i] + distance[j]

				
	total_v = graph.get_total_v()

	new_graph = add_vertice(graph,[0]*(total_v + 1))
	new_total_v = new_graph.get_total_v()

	distance_bf = bellman_ford(new_graph, new_total_v - 1)

	graph_matrix = graph.get_matrix(type)
	transform_vertices(graph_matrix, distance_bf)

	result = []
	for i in range(len(graph_matrix)):
		result.append(dijkstra(Graph(graph_matrix), i))

	rollback_vertices(result, distance_bf)	

	return result


if __name__ == "__main__":

	inf = infinity
	graph = Graph([ [ 0 , -2,inf,inf,inf,inf],
					[inf, 0 , -1,inf,inf,inf],
					[ 4 ,inf, 0 , 2 ,inf, -3],
					[inf,inf,inf, 0 ,inf,inf],
					[inf,inf,inf, 1 , 0 , -4],
					[inf,inf,inf,inf,inf, 0 ]])

	print_m(johnson(graph))
