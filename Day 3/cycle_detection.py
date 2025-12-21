def has_cycle(graph):
    visited = set()      # Visited anywhere in the past
    rec_stack = set()    # Visited in the CURRENT recursion path

    def dfs_cycle_check(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs_cycle_check(neighbor):
                    return True
            elif neighbor in rec_stack:
                # Found a neighbor that is already in our current path!
                return True 

        rec_stack.remove(node) # Backtracking: remove from current path stack
        return False

    # Loop through all nodes (to handle disconnected graphs)
    for node in graph:
        if node not in visited:
            if dfs_cycle_check(node):
                return True
    return False

# --- Test ---
cycle_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'] # Cycle back to A
}

no_cycle_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': []
}

print(f"Cycle in Graph 1: {has_cycle(cycle_graph)}")     # Output: True
print(f"Cycle in Graph 2: {has_cycle(no_cycle_graph)}")  # Output: False