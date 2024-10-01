def check_cell(cellN,visited, x, y):
    if 0 <= x < cellN and 0 <= y < cellN:
        return not visited[x][y]
    return False

def check_solver_cell(cellN, maze, visited, x, y):
    return (0 <= x < cellN and
                0 <= y < cellN and
                maze[x][y] == 0 and
                not visited[x][y])