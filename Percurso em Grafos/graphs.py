import math
infinity = math.inf

class Graph:
	def __init__(self, matrix):
		num_vertices = len(matrix)
		for i in matrix:
			if len(i) != num_vertices:
				raise Exception('Missing vertices in adjacency matrix on line '+ str(i) +' | code 01')
		self.__matrix = matrix

	def __str__(self):
		return self.__print_matix()

	def get_matrix(self):
		return self.__matrix

	def get_adj_list(self, index: int):
		adj = []
		for i in range(len(self.__matrix[index])):
			if self.__matrix[index][i] != infinity:
				adj.append(i)
		return adj

	def get_total_v(self):
		return len(self.__matrix)

	def __print_matix(self):
		graph = self.__matrix
		text = ''
		text += 'Ver.\t'
		vertices_size = len(graph)
		for v in range(vertices_size):
			text +='('+str(v+1)+')\t'
		text += '\n'
		for i in range(vertices_size):
			text += '('+str(i+1)+')\t'
			for j in range(len(graph)):
				text += str(graph[i][j])+'\t'
			text += '\n'
		return text
