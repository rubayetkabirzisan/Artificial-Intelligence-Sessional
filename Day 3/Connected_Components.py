from collections import deque

def bfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    # Queue stores coordinates (row, col)
    queue = deque([start]) 
    visited = set([start])
    
    # Directions: Right, Left, Down, Up
    directions = [(0,1), (0,-1), (1,0), (-1,0)] 
    
    while queue:
        r, c = queue.popleft()
        
        # Check if we reached the goal
        if (r, c) == goal: 
            return True
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check bounds (is inside grid?) and walls (is not 1?)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    
    return False

# --- Test Case ---
sample_grid = [
    [0, 0, 0, 0, 0],  # (0,0) Start
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]   # (4,4) Goal
]

start_pos = (0, 0)
goal_pos = (4, 4)

if bfs_grid(sample_grid, start_pos, goal_pos):
    print("Success: A path exists!")
else:
    print("Failure: No path found.")