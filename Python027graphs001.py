# Implementation of Graphs, using Adjacency Matrix

import numpy as np


def main():
    # graph = Graph(4 )
    # graph.add_edge(3, 1)
    # print(graph.has_selfLoop())
    # graph.add_edge(1,1)
    # print(graph)
    # print(graph.has_selfLoop())
    
    graph = Graph(3)
    edges = [[1, 2], [0, 2], [0, 1]]
    graph.add_edges(edges)
    print(graph)
     
class Graph:
    def __init__(self, n): # n is the number of vertices
        self.graph = np.zeros((n, n))
        self.num_vertices = n

    def __str__(self):
        return f"Graph: {self.graph}"
    
    def add_edge(self, u, v):
        if u < self.num_vertices and v < self.num_vertices:
            self.graph[u][v] = 1
            self.graph[v][u] = 1
            
    def remove_edge(self, u, v):
        if u < self.num_vertices and v < self.num_vertices:
            self.graph[u][v] = 0
            self.graph[v][u] = 0
            
    def has_selfLoop(self):
        if 1 in np.diag(self.graph):
            return True
        return False
    
    def add_edges(self, edges): # edges is a 2d array. eg. [[1, 2], [0, 2], [0, 1]]
        for i in range(len(edges)):
            for j in edges[i]:
                self.graph[i][j] = 1   
    
        
    
if __name__ == "__main__":
    main()
