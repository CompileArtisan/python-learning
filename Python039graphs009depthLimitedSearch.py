import Python029graphs003adjacencyList

def main():
    graph = Python029graphs003adjacencyList.Graph([1, 2, 3, 4, 5, 6, 7])
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 6)
    graph.add_edge(2, 7)
    graph.add_edge(1, 4)
    graph.add_edge(5, 1)
    print(depthLimitedSearch(graph.graph, 1, 2))
    
def depthLimitedSearch(graph, start, limit):
    stack = [(start, 0)]
    visited = []
    
    while stack:
        vertex, depth = stack.pop()
        if vertex not in visited and depth < limit:
            visited.append(vertex)
            stack.extend((neighbor, depth + 1) for neighbor, _ in graph[vertex] if neighbor not in visited)
    return visited

if __name__ == "__main__":
    main()