from collections import deque

def bfs(graph, start_node):
    # 1. Initialize Queue with start node
    queue = deque([start_node])
    
    # 2. Keep track of visited nodes to avoid loops
    visited = set([start_node])
    
    print(f"BFS Traversal starting from {start_node}:")
    
    while queue:
        # 3. Dequeue: Remove the first element (FIFO)
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # 4. Explore Neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Enqueue new neighbors
    print() # Newline

# Run it
# The Graph Structure
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
bfs(graph, 'A')