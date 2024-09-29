def main():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2), ('G', 6)],
        'E': [('B', 5), ('G', 2)],
        'F': [('C', 3), ('G', 1)],
        'G': [('D', 6), ('E', 2), ('F', 1) ]
    }
    print(dijkstra(graph, 'A'))
    
def dijkstra(graph, start):
    visited = [start]
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    
    while len(visited) < len(graph):
        min_vertex = None
        min_distance = float("inf")
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    distance = distances[vertex] + weight
                    if distance < min_distance:
                        min_vertex = neighbor
                        min_distance = distance
        visited.append(min_vertex)
        distances[min_vertex] = min_distance
    return distances

def bellmanFord(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                distance = distances[vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
    return distances

if __name__ == "__main__":
    main()