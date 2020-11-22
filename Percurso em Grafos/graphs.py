import math
infinity = math.inf
import copy

class Graph:
    def __init__(self, matrix):
        num_vertices = len(matrix)
        for i in matrix:
            if len(i) < num_vertices:
                raise Exception(
                    'Missing vertices in adjacency matrix on line ' + str(i) + ' | code 01')
            if len(i) > num_vertices:
                raise Exception(
                    'Too much vertices in adjacency matrix on line ' + str(i) + ' | code 02')
        self.__matrix = matrix

    def __str__(self):
        return self.__print_matix()

    def get_matrix(self, type: str ='ref') -> list:
        if type == 'ref':
            return self.__matrix
        elif type == 'copy':
            return copy.deepcopy(self.__matrix)
        

    def get_adj_list(self, index: int) -> list:
        adj = []
        for i in range(len(self.__matrix[index])):
            if self.__matrix[index][i] != infinity:
                if index != i: 
                    adj.append(i)
        return adj

    def get_total_v(self) -> int:
        return len(self.__matrix)

    def __print_matix(self):
        graph = self.__matrix
        text = ''
        text += 'Ver.\t'
        vertices_size = len(graph)
        for v in range(vertices_size):
            text += '('+str(v)+')\t'
        text += '\n'
        for i in range(vertices_size):
            text += '('+str(i)+')\t'
            for j in range(len(graph)):
                text += str(graph[i][j])+'\t'
            text += '\n'
        return text

    def has_negative_cycle(self) -> bool:
        def get_way_size(source: int, target: int, visited:int):
            if source == target:
                return 0
            if visited[source] == True:
                return infinity

            total_way_size = []
            for i in self.get_adj_list(source):
                visited[source] = True
                total_way_size.append(get_way_size(i, target, visited) + self.__matrix[source][i])

            return min(total_way_size) if len(total_way_size) > 0 else infinity

        total_v = self.get_total_v()
        has_cycle = False
        for i in range(total_v):
            adj_list = self.get_adj_list(i)
            visited = [False] * total_v
            for j in adj_list:
                min_way = get_way_size(j, i, visited) + self.__matrix[i][j]
                if min_way < 0:
                    has_cycle = True

        return has_cycle


def add_vertice(graph: Graph, create_weight: list, set_weight: list=None)->Graph:
    total_v = graph.get_total_v()
    if len(create_weight) > total_v + 1:
        raise Exception('Too much weights to create new vertice | code 03')
    if len(create_weight) < total_v + 1:
        raise Exception('Missing weights to create new vertice | code 04')

    if set_weight == None:
        set_weight = [infinity] * total_v
    else:
        if len(set_weight) > total_v:
            raise Exception('More weights than vertices | code 05')
        if len(set_weight) < total_v:
            raise Exception('Less weights then vertice | code 06')

    matrix = graph.get_matrix('copy')
    for i in range(len(matrix)):
        matrix[i].append(set_weight[i])

    matrix.append(create_weight)

    return Graph(matrix)

def remove_vertice(graph: Graph, vertice: int)->Graph:
    total_v = graph.get_total_v()
    if total_v <= vertice or vertice < 0:
        raise Exception('Invalid vertice index ['+str(vertice)+'] | code 07')
    
    matrix = graph.get_matrix('copy')
    del(matrix[vertice])
    for i in range(len(matrix)):
        del(matrix[i][vertice])

    return Graph(matrix)

def print_m(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t')
        print()
