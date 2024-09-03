import Python029graphs003adjacencyList

def main():
    graph = Python029graphs003adjacencyList.Graph([1, 2, 3, 4, 5, 6, 7])
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 6)
    graph.add_edge(2, 7)
    graph.add_edge(1, 4)
    graph.add_edge(5, 1)
    print(depthLimitedSearch(graph.graph, 1, 7, 3)) 
    
def depthLimitedSearch(graph, start, goal, limit):
    visited = set()
    return recursiveDLS(graph, start, goal, limit, visited)

def recursiveDLS(graph, current, goal, limit, visited):
    if current == goal:
        return True
    if limit <= 0:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            if recursiveDLS(graph, neighbor, goal, limit-1, visited):
                return True
    return False

if __name__ == "__main__":
    main()