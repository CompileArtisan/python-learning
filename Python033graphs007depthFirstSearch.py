import Python029graphs003adjacencyList

def main():
    # graph = Python029graphs003adjacencyList.Graph([1, 2, 3, 4, 5, 6, 7])
    # graph.add_edge(1, 2)
    # graph.add_edge(2, 3)
    # graph.add_edge(2, 6)
    # graph.add_edge(2, 7)
    # graph.add_edge(1, 4)
    # graph.add_edge(5, 1)
    
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2), ('G', 6)],
        'E': [('B', 5), ('G', 2)],
        'F': [('C', 3), ('G', 1)],
        'G': [('D', 6), ('E', 2), ('F', 1) ]
    }

    print(depthFirstSearch(graph, 'A'))
    print(depthLimitedSearch(graph, 'A', 2))

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

def depthLimitedSearch(graph, start, limit):
    stack = [(start, 0)]
    visited = []

    while stack:
        vertex, depth = stack.pop()
        if vertex not in visited and depth <= limit:
            visited.append(vertex)
            stack.extend((neighbor, depth + 1) for neighbor, _ in graph[vertex] if neighbor not in visited)
            # add all of the neighbours to the stack 👆
    return visited

def iterativeDeepeningSearch(graph, start, max_depth):
    for limit in range(max_depth):
        result = depthLimitedSearch(graph, start, limit)
        if len(result) < max_depth:
            return result
    return result

if __name__ == "__main__":
    main()