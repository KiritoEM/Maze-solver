import pygame
from helpers.constant import color

class Game:
    def __init__(self, window_width, window_height, maze, algo):
        self.window_width = window_width
        self.window_height = window_height
        self.maze = maze
        self.algo = algo
        self.cellN = maze.cellN
        self.cell_width = window_width / self.cellN
        self.cell_height = window_height / self.cellN
        self.black = pygame.Color("black")
        self.white = pygame.Color("white")
        self.blue = pygame.Color("blue")
        self.orange = pygame.Color("darkorange")
        self.brown = pygame.Color(color["BROWN"])
        self.grey = pygame.Color(color["GREY"])
        self.green = pygame.Color(color["GREEN"])
        self.red = pygame.Color(color["RED"])
        self.window = None
        self.startPosition = (0, 0)
        self.finalPosition = (self.cellN - 1, self.cellN - 1)

    def draw_cell(self, row, col, color):
        pygame.draw.rect(self.window, color, (col * self.cell_width, row * self.cell_height, self.cell_width + 1, self.cell_height + 1))

    def draw_bot(self, row, col, color):
        bot_width = self.cell_width // 2
        bot_height = self.cell_height // 2
        bot_x = (col * self.cell_width) + (self.cell_width - bot_width) // 2
        bot_y = (row * self.cell_height) + (self.cell_height - bot_height) // 2
        pygame.draw.rect(self.window, color, (bot_x, bot_y, bot_width, bot_height))

    def draw_grid_on_walls(self):
        for i in range(self.cellN):
            for j in range(self.cellN):
                if self.maze.maze[i][j] == 1:
                    pygame.draw.line(self.window, self.brown, (j * self.cell_width, i * self.cell_height), ((j + 1) * self.cell_width, i * self.cell_height), 3)
                    pygame.draw.line(self.window, self.brown, (j * self.cell_width, i * self.cell_height), (j * self.cell_width, (i + 1) * self.cell_height), 3)
                    pygame.draw.line(self.window, self.brown, ((j + 1) * self.cell_width, i * self.cell_height), ((j + 1) * self.cell_width, (i + 1) * self.cell_height), 3)
                    pygame.draw.line(self.window, self.brown, (j * self.cell_width, (i + 1) * self.cell_height), ((j + 1) * self.cell_width, (i + 1) * self.cell_height), 3)

    def update_display(self):
        self.draw_maze()
        pygame.display.flip()

    def move_bot(self, path):
        self.draw_maze()
        current_position = None
        for step in path:
            if len(step) == 2:
                row, col = step
                if current_position:
                    self.update_display()
                    self.draw_bot(current_position[0], current_position[1], self.black)
                self.update_display()
                self.draw_bot(row, col, self.green)
                current_position = (row, col)
                pygame.display.update()
                pygame.time.wait(350)  
            elif len(step) == 3:
                self.update_display()
                row, col, action = step
                if action == "backtrack":
                    self.draw_bot(row, col, self.red)
                    pygame.display.update()
                    pygame.time.wait(350)  

    def draw_maze(self):
        for i in range(self.cellN):
            for j in range(self.cellN):
                if self.maze.maze[i][j] == 0:
                    self.draw_cell(i, j, self.black)
                else:
                    self.draw_cell(i, j, self.grey)
        self.draw_grid_on_walls()
        end_x, end_y = self.finalPosition
        self.draw_cell(end_x, end_y, self.red)

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze Solver")
        self.window.fill(self.brown)

        start_x, start_y = self.startPosition
        end_x, end_y = self.finalPosition

        self.maze.generate_maze(start_x, start_y, self)  # maze Generating

        self.algo.solve(start_x, start_y, end_x, end_y)  # algo solving
        path = self.algo.path

        self.algo.print_solution()

        RUNNING = True
        while RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

            if path:
                self.move_bot(path)
                RUNNING = False

            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            pygame.display.flip()
