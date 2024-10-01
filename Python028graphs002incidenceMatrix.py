# implementation of graphs using incidence matrix

def main():
    graph = Graph(3, 3)
    vertices = [0, 1, 2]
    edges = [[1, 2], [0, 2], [0, 1]] # edge 1->2, 0->2, 0->1
    graph.add_edges(edges)
    print(graph)
    
class Graph:
    # Vertices is a list of vertices
    # Edges is a list of tuples. Each edge is 1 tuple
    # rows: vertices, columns: edges
    
    # basically, incidence matrix tells you if an edge is associated with a node or not
    # +1 if an edge is directed outwards from that node
    # -1 if an edge is directed in to that node
    
    def __init__(self, No_Of_vertices, No_Of_edges):
        self.graph = [[0] * No_Of_edges for _ in range(No_Of_vertices)]
        
    def __str__(self):
        strr = ""
        for i in self.graph:
            strr += str(i) + "\n"
        return strr
    
    
    def add_edges(self , edges):
        for i in range(len(edges)):
            self.graph[edges[i][0]][i] = 1
            self.graph[edges[i][1]][i] = -1
    
    
if __name__ == "__main__":
    main()