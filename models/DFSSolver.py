import pygame
from helpers.mazeHelper import check_solver_cell

class DFSSolver:
    def __init__(self, maze, cellN):
        self.maze = maze
        self.visited = [[False] * cellN for _ in range(cellN)] # Defautl False
        self.path = []
        self.cellN = cellN

    def check_neighbors(self, x, y):
        neighbors = []
        
        directions = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)] # W -> W -> S -> E

        for nx, ny in directions:
            if check_solver_cell(self.cellN, self.maze, self.visited,  nx, ny ):
                neighbors.append((nx, ny))

        return neighbors if neighbors else []

    def dfs(self, x, y, final_x, final_y):
        if not check_solver_cell(self.cellN, self.maze,  self.visited,  x, y ): #if visited then false
            return False
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

        self.visited[x][y] = True
        self.path.append((x, y))

        if (x, y) == (final_x, final_y): # Check if finished maze
            return True
        
        neighbors  = self.check_neighbors(x, y)

        for new_x, new_y in neighbors:
                if self.dfs(new_x, new_y, final_x, final_y):
                    return True

        # self.path.append((x, y, "backtrack")) # Backtracking
        self.path.pop()
        return False

    def solve(self, start_x, start_y, final_x, final_y):
        self.path = []
        self.visited = [[False] * self.cellN for _ in range(self.cellN)]
        if self.dfs(start_x, start_y, final_x, final_x):
            return self.path
        else:
            return []

    def print_solution(self):
        print(self.path)
        for row in self.visited:
            print(' '.join(str(int(cell)) for cell in row))
        print("\n")


