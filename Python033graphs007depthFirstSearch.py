import Python029graphs003adjacencyList

def main():
    graph = Python029graphs003adjacencyList.Graph([1, 2, 3, 4, 5, 6, 7])
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 6)
    graph.add_edge(2, 7)
    graph.add_edge(1, 4)
    graph.add_edge(5, 1)
    print(depthFirstSearch(graph.graph, 1))

def depthFirstSearch(graph, start):
    stack = [start]
    visited = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(neighbor for neighbor, _ in graph[vertex] if neighbor not in visited)
            # add all of the neighbours to the stack 👆
    return visited

if __name__ == "__main__":
    main()