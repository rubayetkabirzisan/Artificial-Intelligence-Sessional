import heapq

def best_first_search(graph, start, goal, heuristics):
    # 1. Initialize Priority Queue
    # Format: (heuristic_value, node_name, path_taken)
    # We start with the 'start' node.
    pq = []
    heapq.heappush(pq, (heuristics[start], start, [start]))
    
    # 2. Keep track of visited nodes to prevent loops
    visited = set()
    
    print(f"Starting Search from {start} to {goal}...\n")

    while pq:
        # 3. Pop the node with the LOWEST heuristic value (The 'Best' node)
        current_h, current_node, path = heapq.heappop(pq)
        
        print(f"Visiting: {current_node} (Heuristic: {current_h})")

        # 4. Check if we reached the goal
        if current_node == goal:
            print("\nGoal Reached!")
            return path

        # 5. Expand neighbors if not visited
        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    neighbor_h = heuristics[neighbor]
                    
                    # Push neighbor to PQ
                    heapq.heappush(pq, (neighbor_h, neighbor, new_path))
                    
    return None

# --- Custom Input Data ---

# Graph Structure (Adjacency List)
# A connects to B and C, etc.
my_graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': ['H'],
    'F': ['I', 'G'],
    'H': [],
    'I': [],
    'G': []
}

# Heuristic Values (Distance estimates to Goal 'G')
# Lower numbers are "better"
my_heuristics = {
    'S': 10,
    'A': 9,
    'B': 4,   # B (4) is better than A (9), so algorithm goes this way
    'C': 9,
    'D': 8,
    'E': 10,
    'F': 2,   # F (2) is better than E (10)
    'H': 15,
    'I': 5,
    'G': 0    # Goal is always 0
}

# Run the Function
path = best_first_search(my_graph, 'S', 'G', my_heuristics)

print("-" * 30)
if path:
    print("Final Path:", " -> ".join(path))
else:
    print("No path found.")