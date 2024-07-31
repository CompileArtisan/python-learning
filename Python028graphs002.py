# implementation of graphs using incidence matrix

def main():
    graph = Graph(3, 3)
    vertices = [0, 1, 2]
    edges = [[1, 2], [0, 2], [0, 1]]
    graph.add_edges(vertices, edges)
    print(graph)
    
class Graph:
    # Vertices is a list of vertices
    # Edges is a list of tuples. Each edge is 1 tuple
    def __init__(self, No_Of_vertices, No_Of_edges):
        self.graph = [[0] * No_Of_edges for _ in range(No_Of_vertices)]
        
    def __str__(self):
        return f"{self.graph}"
    
    def add_edges(self ,vertices, tuples):
        for i in range(len(tuples)):
            for j in tuples[i]:
                self.graph[i][j] = 1
    
    
if __name__ == "__main__":
    main()