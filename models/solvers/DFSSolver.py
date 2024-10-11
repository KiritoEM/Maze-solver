import pygame
from helpers.mazeHelper import check_solver_cell
from .Solver import Solver

class DFSSolver(Solver):
    def __init__(self, maze, cellN):
        super().__init__(maze, cellN)
        self.maze = maze
        self.cellN = cellN

    def dfs(self, x, y, final_x, final_y):
        if not check_solver_cell(self.cellN, self.maze, self.visited, x, y):
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        self.visited[x][y] = True
        self.path.append((x, y))

        if (x, y) == (final_x, final_y):
            return True

        neighbors = self.check_neighbors(x, y)

        for new_x, new_y in neighbors:
            if self.dfs(new_x, new_y, final_x, final_y):
                return True

        self.path.pop()
        return False

    def solve(self, start_x, start_y, final_x, final_y):
        self.path = []
        self.visited = [[False] * self.cellN for _ in range(self.cellN)]
        if self.dfs(start_x, start_y, final_x, final_y):
            return self.path
        else:
            return []
