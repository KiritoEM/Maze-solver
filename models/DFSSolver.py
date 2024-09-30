from .Maze import Maze

class DFSSolver:
    def __init__(self, maze, cellRows, cellColsols):
        self.maze = maze
        self.visited = [[False for _ in range(cellColsols)] for _ in range(cellRows)]
        self.cellRows = cellRows
        self.cellColsols = cellColsols
        self.paths = []  
        self.stack = []

    def check_cell(self, x, y):
        return (0 <= x < self.cellRows and 0 <= y < self.cellColsols and 
                self.maze[x][y] == 0 and not self.visited[x][y])

    def check_directions(self, x, y):
        directions = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        possible_directions = []

        for new_x, new_y in directions:
            if self.check_cell(new_x, new_y):
                possible_directions.append((new_x, new_y))
        
        return possible_directions if len(possible_directions) > 0 else []

    def dfs(self, start_x, start_y):
        self.stack = [(start_x, start_y)]
        self.paths = [(start_x, start_y)]
        self.visited[start_x][start_y] = True

        while self.stack:
            x, y = self.paths[-1] 

            if x == self.cellRows - 1 and y == self.cellColsols - 1: #point d' arrivée
                self.paths.append((x, y)) 
                return True 
        
            directions = self.check_directions(x, y)

            if len(directions) > 0: 
                new_x, new_y = directions.pop()
                self.paths.append((new_x, new_y))
                self.visited[new_x][new_y] = True
                self.paths.append((new_x, new_y))
                self.stack.append((new_x, new_y)) 
            else:
                self.stack.pop()  
                self.paths.pop()      
            

        return False

    def print_solution(self):
        for row in self.visited:
            print(' '.join(str(int(cell)) for cell in row))
        print("\n")
