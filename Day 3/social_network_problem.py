from collections import deque

def degrees_of_separation(graph, start_person, target_person):
    if start_person == target_person:
        return 0
    
    # Queue stores tuples: (current_person, distance_from_start)
    queue = deque([(start_person, 0)])
    visited = set([start_person])
    
    while queue:
        current_person, dist = queue.popleft()
        
        if current_person == target_person:
            return dist
            
        for friend in graph.get(current_person, []):
            if friend not in visited:
                visited.add(friend)
                # Add friend to queue, distance increases by 1
                queue.append((friend, dist + 1))
                
    return -1 # Connection not found

# --- Test ---
social_graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David'],
    'Charlie': ['Alice', 'Eve'],
    'David': ['Bob'],
    'Eve': ['Charlie', 'Frank'],
    'Frank': ['Eve']
}

print(f"Degrees: {degrees_of_separation(social_graph, 'Alice', 'Frank')}") 
# Output: Degrees: 3 (Alice -> Charlie -> Eve -> Frank)