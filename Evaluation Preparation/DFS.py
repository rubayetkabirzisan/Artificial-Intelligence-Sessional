def dfs_iterative(graph, start_node):
    # 1. Initialize Stack with start node
    stack = [start_node]
    visited = set([start_node])
    
    print(f"DFS Traversal starting from {start_node}:")
    
    while stack:
        # 3. Pop: Remove the LAST element added (LIFO)
        current_node = stack.pop()
        print(current_node, end=" ")
        
        # 4. Explore Neighbors
        # We reverse neighbors here just to visit left-to-right 
        # (Since stack pops the last item added, we add right neighbor then left neighbor)
        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    print()

# Run it
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
dfs_iterative(graph, 'A')