import heapq

def greedy_best_first_search(graph, start, goal, h_values):
    """
    Implements Greedy Best First Search using a Priority Queue.
    
    :param graph: Dictionary representing the adjacency list
    :param start: Starting node (string)
    :param goal: Goal node (string)
    :param h_values: Dictionary containing heuristic values for each node
    :return: List of nodes representing the path, or None if no path found
    """
    
    # Priority Queue stores tuples: (heuristic_value, current_node, path_so_far)
    # heapq always pops the item with the lowest first element (lowest h)
    pq = [(h_values[start], start, [start])]
    
    # Set to keep track of visited nodes to avoid cycles
    visited = set()

    while pq:
        # Get the node with the lowest heuristic value
        (h, current_node, path) = heapq.heappop(pq)

        # 1. Goal Check
        if current_node == goal:
            return path

        # 2. Expansion
        if current_node not in visited:
            visited.add(current_node)
            
            # Check if node has neighbors in the graph
            if current_node in graph:
                for neighbor, cost in graph[current_node]:
                    if neighbor not in visited:
                        # Create the new path history
                        new_path = path + [neighbor]
                        
                        # Add to priority queue
                        # Priority is based ONLY on h(neighbor)
                        heapq.heappush(pq, (h_values[neighbor], neighbor, new_path))
                        
    return None

# --- Driver Code ---

if __name__ == "__main__":
    # 1. Define the Graph (Adjacency List)
    # Structure: 'Node': [('Neighbor', edge_cost)]
    my_graph = {
        'S': [('A', 1), ('B', 1)],
        'A': [('C', 1), ('D', 1)],
        'B': [('E', 1), ('F', 1)],
        'C': [],
        'D': [],
        'E': [('H', 1)],
        'F': [('I', 1), ('G', 1)],
        'H': [],
        'I': [],
        'G': []
    }

    # 2. Define Heuristics (h) - Estimated distance to goal 'G'
    # 'S' is Start, 'G' is Goal (h=0)
    my_heuristics = {
        'S': 10,
        'A': 9,
        'B': 4,  # B has lower h, so the algorithm will pick B over A
        'C': 9,
        'D': 8,
        'E': 10,
        'F': 2,
        'H': 15,
        'I': 5,
        'G': 0
    }

    # 3. Run the search
    start_node = 'S'
    goal_node = 'G'
    result_path = greedy_best_first_search(my_graph, start_node, goal_node, my_heuristics)

    # 4. Output results
    if result_path:
        print(f"Success! Path found: {' -> '.join(result_path)}")
    else:
        print("Failure: No path found.")