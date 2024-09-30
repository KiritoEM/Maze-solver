import pygame

class DFSSolver:
    def __init__(self, maze, cellN):
        self.maze = maze
        self.visited = [[False] * cellN for _ in range(cellN)]
        self.cellN = cellN
        self.path = []

    def is_valid_cell(self, x, y):
        return (0 <= x < self.cellN and
                0 <= y < self.cellN and
                self.maze[x][y] == 0 and
                not self.visited[x][y])

    def dfs(self, x, y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if not self.is_valid_cell(x, y):
            return False

        self.visited[x][y] = True
        self.path.append((x, y))

        if (x, y) == (0, 0):
            return True

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.dfs(new_x, new_y):
                return True

        self.path.pop()
        return False

    def solve(self, start_x=0, start_y=0):
        self.path = []
        self.visited = [[False] * self.cellN for _ in range(self.cellN)]
        if self.dfs(start_x, start_y):
            return self.path
        else:
            return []

    def print_solution(self):
        """Affiche le chemin trouvé."""
        for row in self.visited:
            print(' '.join(str(int(cell)) for cell in row))
        print("\n")
