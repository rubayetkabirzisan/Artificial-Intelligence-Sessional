from collections import deque

def shortest_path_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    start_r, start_c = start
    
    # Queue stores tuple: (row, col, steps_taken)
    queue = deque([(start_r, start_c, 0)])
    
    # Visited set stores (row, col) to prevent loops
    visited = set([(start_r, start_c)])
    
    # Directions: Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    print(f"BFS Search started at {start}...")
    
    while queue:
        r, c, steps = queue.popleft()
        
        # Check if we reached the goal
        if (r, c) == goal:
            return steps # Return the number of steps
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check Bounds (is it inside grid?) AND Walls (is it not 1?)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Add to queue, increment steps by 1
                    queue.append((nr, nc, steps + 1))
                    
    return -1 # Return -1 if no path exists

# --- Test Case ---
# 0 = Open path, 1 = Wall
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start_pos = (0, 0) # Top-Left
goal_pos = (3, 3)  # Bottom-Right

steps = shortest_path_maze(grid, start_pos, goal_pos)

if steps != -1:
    print(f"Shortest path found! It takes {steps} steps.")
else:
    print("No path possible.")