from helpers.mazeHelper import check_solver_cell

class Solver:
    def __init__(self, maze, cellN) :
        self.maze = maze
        self.visited = [[False] * cellN for _ in range(cellN)]
        self.path = []
    
    def get_path(self):
        return self.path
        
    def check_neighbors(self, x, y):
        neighbors = []

        directions = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]  # Directions: W -> N -> S -> E

        for nx, ny in directions:
            if 0 <= nx < self.cellN and 0 <= ny < self.cellN:
                    if check_solver_cell(self.cellN, self.maze, self.visited, nx, ny):
                        neighbors.append((nx, ny))

        return neighbors
        
    def print_solution(self):
        for row in self.visited:
            print(' '.join(str(int(cell)) for cell in row))
        print("\n")


