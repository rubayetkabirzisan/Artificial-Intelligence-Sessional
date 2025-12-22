def is_safe(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    if 3 - m > 0 and 3 - c > 3 - m:
        return False
    return True

start_state = (3, 3, 0)
goal_state = (0, 0, 1)

queue = []
queue.append([start_state, [start_state]])
visited = []

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

while len(queue) > 0:
    current_node = queue.pop(0)
    state = current_node[0]
    path = current_node[1]

    if state == goal_state:
        for step in path:
            print(step)
        break

    if state in visited:
        continue
    
    visited.append(state)

    m, c, b = state

    for move in moves:
        dm, dc = move
        
        if b == 0:
            new_state = (m - dm, c - dc, 1)
        else:
            new_state = (m + dm, c + dc, 0)

        if is_safe(new_state):
            new_path = path + [new_state]
            queue.append([new_state, new_path])