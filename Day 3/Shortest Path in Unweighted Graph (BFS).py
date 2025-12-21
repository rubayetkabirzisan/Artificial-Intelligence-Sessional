from collections import deque

def shortest_path_bfs(graph, start, goal):
    # Initialize Queue with tuple: (current_node, path_so_far)
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Check if we reached the goal
        if current == goal:
            return path # Found it!
        
        # Explore neighbors
        for neighbor in graph.get(current, []): # .get() avoids crash if node has no entry
            if neighbor not in visited:
                visited.add(neighbor)
                # Append neighbor to the current path and add to queue
                queue.append((neighbor, path + [neighbor]))
                
    return None # Return None if goal is not reachable

# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Run and PRINT the result
result = shortest_path_bfs(graph, 'A', 'F')
print(f"Shortest Path from A to F: {result}")