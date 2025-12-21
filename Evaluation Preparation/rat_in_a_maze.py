def solve_maze_dfs(maze, r, c, visited):
    rows, cols = len(maze), len(maze[0])
    
    # 1. Base Cases (Stop conditions)
    # Out of bounds OR Hit a wall (1)
    if r < 0 or c < 0 or r >= rows or c >= cols or maze[r][c] == 1:
        return False
    # Already visited this cell
    if (r, c) in visited:
        return False
    # Reached Goal (Bottom-Right corner)
    if r == rows - 1 and c == cols - 1:
        return True
    
    # 2. Mark current cell as visited
    visited.add((r, c))
    
    # 3. Explore Neighbors (Down, Right, Up, Left)
    # Using 'or' means if ANY path returns True, we succeed
    if (solve_maze_dfs(maze, r+1, c, visited) or  # Down
        solve_maze_dfs(maze, r, c+1, visited) or  # Right
        solve_maze_dfs(maze, r-1, c, visited) or  # Up
        solve_maze_dfs(maze, r, c-1, visited)):   # Left
        return True
        
    return False

# --- Test ---
maze_grid = [
    [0, 1, 0, 0], # Start at top-left (0,0)
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]  # Goal is bottom-right
]

# Start recursion at (0,0) with an empty visited set
result = solve_maze_dfs(maze_grid, 0, 0, set())
print(f"Path exists: {result}") 
# Output: Path exists: True