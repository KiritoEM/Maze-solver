import pygame
from random import choice, shuffle

class Maze:
    def __init__(self, cellN):
        self.cellN = cellN
        self.board = [[1] * cellN for _ in range(cellN)]
        self.visited = [[False] * cellN for _ in range(cellN)]
        self.stack = []

    def check_cell(self, x, y):
        if 0 <= x < self.cellN and 0 <= y < self.cellN:
            return not self.visited[x][y]
        return False

    def check_neighbors(self, x, y):
        neighbors = []

        directions = [
            (x, y - 2),
            (x, y + 2),
            (x - 2, y),
            (x + 2, y)
        ]

        for nx, ny in directions:
            if self.check_cell(nx, ny):
                neighbors.append((nx, ny))

        shuffle(neighbors)
        return choice(neighbors) if neighbors else False

    def generate_maze(self, startX, startY, game):
        self.stack = [(startX, startY)]
        self.visited[startX][startY] = True
        self.board[startX][startY] = 0

        while self.stack:
            x, y = self.stack[-1]
            neighbor = self.check_neighbors(x, y)

            if neighbor:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                nx, ny = neighbor

                self.board[x + (nx - x) // 2][y + (ny - y) // 2] = 0
                self.board[nx][ny] = 0
                self.visited[nx][ny] = True
                self.stack.append((nx, ny))
            else:
                self.stack.pop()  # Backtracking

            game.update_display()
            pygame.time.wait(50)

    def print_maze(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

    def getBoard(self):
        return self.board

    def set_start_position(self, startX, startY):
        self.board[startX][startY] = 0
