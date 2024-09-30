import pygame

import pygame

class Game:
    def __init__(self, window_width, window_height, maze, DFS):
        self.window_width = window_width
        self.window_height = window_height
        self.maze = maze
        self.DFS = DFS
        self.cellRows = maze.cellRows
        self.cellCols = maze.cellCols
        self.cell_width = window_width / self.cellRows
        self.cell_height = window_height / self.cellCols
        self.black = pygame.Color("black")
        self.white = pygame.Color("white")
        self.orange = pygame.Color("darkorange")
        self.window = None

    def draw_cell(self, row, col, color):
        pygame.draw.rect(self.window, color, (col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height))
    
    def draw_circle(self, row, col, color):
        pygame.draw.circle(self.window, color, (col * self.cell_width + self.cell_width // 2, row * self.cell_height + self.cell_height // 2), 14)


    def draw_grid(self):
        for i in range(self.cellRows + 1):
            pygame.draw.line(self.window, self.orange, (0, i * self.cell_height), (self.window_width, i * self.cell_height))
        for j in range(self.cellCols + 1):
            pygame.draw.line(self.window, self.orange, (j * self.cell_width, 0), (j * self.cell_width, self.window_height))

    def draw_board(self):
        for i in range(self.cellRows):
            for j in range(self.cellCols):
                if self.maze.board[i][j] == 0:  # Path
                    self.draw_cell(i, j, self.white)
                else:
                    self.draw_cell(i, j, self.black)
        # self.draw_grid()

    def update_display(self):
        self.window.fill(self.black)
        self.draw_board()
        pygame.display.update()

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze Solver")
        self.window.fill(self.white)

        self.maze.generate_maze(0, 0, self)
        # self.maze.print_maze()

        self.DFS.dfs(0, 0)  
        self.DFS.print_solution()  

        RUNNING = True
        while RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

            self.draw_board()
            pygame.display.update()

        pygame.quit()
