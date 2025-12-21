import collections

def bfs_shortest_path(grid, start, goal):
    """
    Finds the shortest path in a grid using BFS.
    Returns a list of coordinates [(r, c), ...] if found, else None.
    """
    # 1. Edge Case: Empty grid or invalid inputs
    if not grid or not grid[0]:
        return None
    
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    gr, gc = goal

    # Validate start/goal are within bounds and not walls
    if not (0 <= sr < rows and 0 <= sc < cols) or grid[sr][sc] == 1:
        return None
    if not (0 <= gr < rows and 0 <= gc < cols) or grid[gr][gc] == 1:
        return None

    # 2. Setup BFS
    queue = collections.deque([start])
    visited = set([start])
    # Parent dictionary to reconstruct the path: {child: parent}
    parent_map = {start: None} 
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

    while queue:
        curr = queue.popleft()
        r, c = curr

        # 3. Goal Check
        if curr == goal:
            return reconstruct_path(parent_map, start, goal)

        # 4. Explore Neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and walls (1 is wall)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent_map[(nr, nc)] = curr
                    queue.append((nr, nc))

    return None # Goal not reachable

def reconstruct_path(parent_map, start, goal):
    """Backtracks from goal to start to build the path list."""
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent_map[curr]
    return path[::-1] # Reverse to get Start -> Goal

def visualize_grid(grid, path):
    """Pretty prints the grid with the path marked as '*'."""
    display_grid = [row[:] for row in grid] # Copy grid
    
    if path:
        for r, c in path:
            display_grid[r][c] = '*' # Mark path
            
    print("-" * 20)
    for row in display_grid:
        # Convert row to string: 1='#' (Wall), 0='.' (Empty), *='*' (Path)
        line = ""
        for cell in row:
            if cell == 1: line += "# "
            elif cell == '*': line += "* "
            else: line += ". "
        print(line)
    print("-" * 20)

# --- Main Execution Block ---
if __name__ == "__main__":
    # 0 = Empty, 1 = Wall
    grid_map = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_pos = (0, 0)
    goal_pos = (4, 4)

    print(f"Start: {start_pos}, Goal: {goal_pos}")
    
    # Run BFS
    path = bfs_shortest_path(grid_map, start_pos, goal_pos)

    if path:
        print(f"Path found! Length: {len(path)}")
        print(f"Coordinates: {path}")
        print("\nVisualization:")
        visualize_grid(grid_map, path)
    else:
        print("No path found.")