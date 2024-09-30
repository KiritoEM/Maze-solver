import pygame

class Game:
    def __init__(self, window_width, window_height, maze, DFS):
        self.window_width = window_width
        self.window_height = window_height
        self.maze = maze
        self.DFS = DFS
        self.cellN = maze.cellN
        self.cell_width = window_width / self.cellN
        self.cell_height = window_height / self.cellN
        self.black = pygame.Color("black")
        self.white = pygame.Color("white")
        self.orange = pygame.Color("darkorange")
        self.green = pygame.Color("green")
        self.window = None

        print(self.cell_height, maze.cellN)

    def draw_cell(self, row, col, color):
        pygame.draw.rect(self.window, color, (col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height))

    def draw_circle(self, row, col, color):
        pygame.draw.circle(self.window, color, (col * self.cell_width + self.cell_width // 2, row * self.cell_height + self.cell_height // 2), 14)

    def draw_grid(self):
        for i in range(self.cellN + 1):
            for j in range(self.cellN + 1):
                if i < self.cellN and j < self.cellN and self.maze.board[i][j] == 1:  # Wall
                    pygame.draw.line(self.window, self.orange, (j * self.cell_width, i * self.cell_height), ((j + 1) * self.cell_width, i * self.cell_height))
                    pygame.draw.line(self.window, self.orange, (j * self.cell_width, i * self.cell_height), (j * self.cell_width, (i + 1) * self.cell_height))

    def draw_board(self):
        for i in range(self.cellN):
            for j in range(self.cellN):
                if self.maze.board[i][j] == 0:  # Path
                    self.draw_cell(i, j, self.black)
                else:
                    self.draw_cell(i, j, self.orange)
        self.draw_grid()

    def update_display(self):
        self.window.fill(self.black)
        self.draw_board()
        pygame.display.flip()

    def draw_path(self, path):
        self.draw_board()
        for (row, col) in path:
            self.draw_cell(row, col, self.green)
            pygame.display.update()
            pygame.time.wait(150)

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze Solver")
        self.window.fill(self.black)

        self.maze.generate_maze(0, 0, self)

        path = self.DFS.solve(self.cellN - 1, self.cellN - 1)

        RUNNING = True
        while RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

            if path:
                self.draw_path(path)
                RUNNING = False  

            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            pygame.display.update()
