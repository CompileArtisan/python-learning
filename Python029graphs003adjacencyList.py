# implementation of graphs using adjacency list
def main():
    graph = Graph([0, 1, 2])
    graph.add_edge(0, 1)
    print(graph.has_selfLoop())
    graph.add_edge(1, 1)
    print(graph)
    print(graph.has_selfLoop())
    graph.remove_edge(1, 1)
    print(graph)
    
class Graph:    
    # Overall Structure:
    # graph is a dictionary: key=vertex, value=list of edges
    # Each edge is a tuple (vertex, weight)
    
    def __init__(self, vertices): # vertices is a list of vertices. Each vertex is a number/character.
        self.graph = {}
        for vertex in vertices:
            self.graph[vertex] = []
            
    def __str__(self):
        result = ""
        for vertex in self.graph:
            result += f"{vertex}: "
            for edge in self.graph[vertex]:
                result += f"{edge[0]}({edge[1]}) "
            result += "\n"
        return result
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        
    def remove_edge(self, u, v):
        self.graph[u] = [edge for edge in self.graph[u] if edge[0] != v]
        self.graph[v] = [edge for edge in self.graph[v] if edge[0] != u]
    
    def has_selfLoop(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                if vertex == edge[0]:
                    return True
        return False
    
if __name__ == "__main__":
    main()