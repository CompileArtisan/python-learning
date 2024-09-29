def uniform_cost_search(graph, start, goal):
    # List to act as the priority queue, storing (cost, node, path)
    priority_queue = [(0, start, [start])]  # (cost, node, path)
    # Keep track of the cost to reach each node
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    # Track visited nodes
    visited = set()

    while priority_queue:
        # Sort the list by cost (first element of the tuple) and pop the lowest cost node
        priority_queue.sort()  # Sorting by cost (smallest first)
        current_cost, current_node, path = priority_queue.pop(0)
        
        # If we've reached the goal, return the cost and path
        if current_node == goal:
            return current_cost, path
        
        # If the node has been visited, skip it
        if current_node in visited:
            continue
        
        # Mark the node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_cost = current_cost + weight
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    priority_queue.append((new_cost, neighbor, path + [neighbor]))
    
    # If the goal was not reachable
    return float('inf'), []

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('G', 6)],
    'E': [('B', 5), ('G', 2)],
    'F': [('C', 3), ('G', 1)],
    'G': [('D', 6), ('E', 2), ('F', 1) ]
}

start = 'A'
goal = 'F'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Cost from {start} to {goal}: {cost}")
print(f"Path from {start} to {goal}: {' -> '.join(path)}")
