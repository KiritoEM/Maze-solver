import pygame

class DFSSolver:
    def __init__(self, maze, cellN):
        self.maze = maze
        self.visited = [[False for _ in range(cellN)] for _ in range(cellN)]
        self.cellN = cellN
        self.path = []
        self.stack = []

    def check_cell(self, x, y):
        return (0 <= x < self.cellN and 0 <= y < self.cellN and
                self.maze[x][y] == 0 and not self.visited[x][y])

    def check_directions(self, x, y):
        directions = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)] # W -> N -> S -> E
        possible_directions = []

        for new_x, new_y in directions:
            if self.check_cell(new_x, new_y):
                possible_directions.append((new_x, new_y))

        return possible_directions if len(possible_directions) > 0 else []

    def dfs(self, start_x, start_y):
        self.path = [(start_x, start_y)]
        self.stack = [(start_x, start_y)]
        self.visited[start_x][start_y] = True

        while len(self.stack) > 0:
            x, y = self.stack.pop()

            if x == self.cellN - 1 and y == self.cellN - 1: # point d' arrivée
                self.path.append((x, y))
                return self.path

            directions = self.check_directions(x, y)
            print("directions: ", directions)

            if len(directions) > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                
                for new_x, new_y in directions:
                    self.stack.append((new_x, new_y))
                    self.path.append((new_x, new_y))
                    self.visited[new_x][new_y] = True

        return self.path

    def print_solution(self):
        for row in self.visited:
            print(' '.join(str(int(cell)) for cell in row))
        print("\n")
