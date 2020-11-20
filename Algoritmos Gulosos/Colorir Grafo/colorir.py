import sys
sys.path.append('../../Percurso em Grafos/')
from graphs import *

def colorir(graph: Graph, src: int):
    total_v = graph.get_total_v()
    vertice_color = [-1] * total_v

    vertice_color[src] = 0

    for v in range(1, total_v):

        colored = [False] * total_v
        
        adj_list = graph.get_adj_list(v)
        for adj in adj_list:
            if vertice_color[adj] != -1:
                colored[vertice_color[adj]] = True

        color = 0
        for v2 in range(total_v):
            if colored[v2] == False:
                color = v2
                break

        vertice_color[v] = color


    return vertice_color


inf = infinity
graph = Graph([ [ 0 ,inf,inf, 1 ,inf,inf,inf],
                [inf, 0 , 1 ,inf, 1 , 1 , 1 ],
                [inf, 1 , 0 ,inf,inf,inf,inf],
                [ 1 ,inf,inf, 0 , 1 ,inf, 1 ],
                [inf, 1 ,inf, 1 , 0 , 1 , 1 ],
                [inf, 1 ,inf,inf, 1 , 0 ,inf],
                [inf, 1 ,inf, 1 , 1 ,inf, 0 ]])

cores = colorir(graph, 0)
for i in range(graph.get_total_v()):
    print(f"Vertice {i} tem cor {cores[i]}")