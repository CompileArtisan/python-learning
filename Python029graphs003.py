# implementation of graphs using adjacency list
def main():
    graph = Graph([0, 1, 2])
    graph.add_edge(0, 1)
    print(graph.has_selfLoop())
    graph.add_edge(1, 1)
    print(graph)
    print(graph.has_selfLoop())
    
class Graph:    
    def __init__(self, vertices): # vertices is a list of vertices. Each vertex is a number.
        self.graph = {}
        for vertex in vertices:
            self.graph[vertex] = []
            
    def __str__(self):
        return f"{self.graph}"
    
    def add_edge(self, u, v):   
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)
    
    def has_selfLoop(self):
        for vertex in self.graph:
            if vertex in self.graph[vertex]:
                return True
        return False
    
if __name__ == "__main__":
    main()