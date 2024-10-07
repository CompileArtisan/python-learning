def main():
    # simple graph as example
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]
    }
    
    print("Prim's Algorithm Output:", prim(graph, 'A'))
    print("Kruskal's Algorithm Output:", kruskal(graph))

# Prim's algorithm
def prim(graph, start):
    visited = set([start])  # Use set for faster lookup
    edges = [] # weight, from, to
    mst = [] # from, to, weight
    
    # Add edges from start node
    for neighbor, weight in graph[start]:
        edges.append((weight, start, neighbor))
    
    while len(visited) < len(graph):
        # Sort edges based on weight
        edges.sort()
        
        # Find the smallest edge that connects to an unvisited node
        for weight, frm, to in edges:
            if to not in visited:
                visited.add(to)
                mst.append((frm, to, weight))
                # Add edges from the newly visited node
                for neighbor, weight in graph[to]:
                    if neighbor not in visited:
                        edges.append((weight, to, neighbor))
                break
    
    return mst

# Kruskal's algorithm
def kruskal(graph):
    edges = []
    mst = []
    
    # Collect all edges from the graph
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    
    # Sort edges by weight
    edges.sort()
    
    parent = {v: v for v in graph}
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            parent[root2] = root1
    
    for weight, v1, v2 in edges:
        if find(v1) != find(v2):
            mst.append((v1, v2, weight))
            union(v1, v2)
    
    return mst

if __name__ == "__main__":
    main()
