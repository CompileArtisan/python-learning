import Python029graphs003

def main():
    graph = Python029graphs003.Graph([1, 2, 3, 4, 5, 6, 7,])
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 6)
    graph.add_edge(2, 7)
    graph.add_edge(1, 4)
    graph.add_edge(5, 1)
    print(depthFirstSearch(graph.graph, 1))
    
def depthFirstSearch(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

if __name__ == "__main__":
    main()
    