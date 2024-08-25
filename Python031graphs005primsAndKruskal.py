
def main():
    # simple graph as example
    graph = {
        0: [(1, 1), (2, 3)],
        1: [(0, 1), (2, 1), (3, 4), (4, 2)],
        2: [(0, 3), (1, 1), (3, 1)],
        3: [(1, 4), (2, 1), (4, 1)],
        4: [(1, 2), (3, 1)]
    }
    
    print(prim(graph, 0))

# prims's algorithm
def prim(graph, start):
    visited = [start]
    edges = []
    
    while len(visited) < len(graph):
        min_edge = None
        min_weight = float("inf")
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited and weight < min_weight:
                    min_edge = (vertex, neighbor)
                    min_weight = weight
        edges.append(min_edge)
        visited.append(min_edge[1])
    return edges

# kruskal's algorithm
def kruskal(graph, start):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((vertex, neighbor, weight))
    edges.sort(key=lambda x: x[2])
    
    visited = [start]
    mst = []
    
    while len(visited) < len(graph):
        min_edge = None
        for edge in edges:
            if edge[0] in visited and edge[1] not in visited:
                min_edge = edge
                break
        mst.append(min_edge)
        visited.append(min_edge[1])
    return mst

    
if __name__ == "__main__":
    main()