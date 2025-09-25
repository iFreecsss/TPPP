from utils import *

# fonction qui ajoute le noeud au graphe
def add_node(graph, node):
    if node not in graph:
        graph[node] = []
    return graph

# fonction qui ajoute une arête entre deux noeuds
def add_edge(graph, node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)
        graph[node2].append(node1)  # pour un graphe non orienté
    return graph
    