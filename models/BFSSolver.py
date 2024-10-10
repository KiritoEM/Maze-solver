from collections import deque
import pygame
from helpers.constant import color

class BFSSolver:
    def __init__(self, maze, cellN):
        self.maze = maze
        self.queue = deque()
        self.visited = [[False] * cellN for _ in range(cellN)]
        self.path = []
        self.finished = False

    def solve(self, start_x, start_y, des_x, des_y):
        self.visited[start_x][start_y] = True
        self.queue.append((start_x, start_y, [(start_x, start_y)]))

        while len(self.queue) > 0 and not self.finished:
            (curr_x, curr_y, current_path) = self.queue.popleft()  # Dequeue the current position
            print(f"Visiting: {(curr_x, curr_y)}")

            if curr_x == des_x and curr_y == des_y:
                self.path = current_path
                self.finished = True
                return

            neighbors = self.check_neighbors(curr_x, curr_y)

            for n_x, n_y in neighbors:
                if not self.visited[n_x][n_y] and self.maze[n_x][n_y] == 0:
                    self.visited[n_x][n_y] = True
                    self.queue.append((n_x, n_y, current_path + [(n_x, n_y)]))

    def check_neighbors(self, x, y):
        neighbors = []
        directions = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]

        for nx, ny in directions:
            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] == 0:
                neighbors.append((nx, ny))

        return neighbors

    def print_solution(self):
        if self.finished:
            print("Path found:")
            for pos in self.path:
                print(pos)
        else:
            print("Destination is inaccessible.")

        print("\nVisited matrix:")
        for row in self.visited:
            print(' '.join(['1' if cell else '0' for cell in row]))
        print()