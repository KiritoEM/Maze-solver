from collections import deque
import pygame
from .Solver import Solver

class BFSSolver(Solver):
    def __init__(self, maze, cellN):
        super().__init__(maze, cellN)
        self.maze = maze
        self.queue = deque()
        self.cellN = cellN

    def get_path(self):
        print("Path from getter: ", self.path)
        return self.path

    def solve(self, start_x, start_y, des_x, des_y):
        print("Starting position:", start_x, start_y)
        self.visited[start_x][start_y] = True
        self.queue.append((start_x, start_y, [(start_x, start_y)]))

        while len(self.queue) > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            curr_x, curr_y, curr_path = self.queue.popleft()

            if curr_x == des_x and curr_y == des_y:
                self.path = curr_path
                return self.path

            neighbors = self.check_neighbors(curr_x, curr_y)

            for n_x, n_y in neighbors:
                if not self.visited[n_x][n_y] and self.maze[n_x][n_y] == 0 and 0 <= n_x < self.cellN and 0 <= n_y < self.cellN:
                    self.visited[n_x][n_y] = True
                    new_path = curr_path + [(n_x, n_y)]
                    self.queue.append((n_x, n_y, new_path))

        return False  
