from views.Game import Game
from models.DFSSolver import DFSSolver
from models.Maze import Maze

def main():
    window_width = 850
    window_height = 700
    cellN = 27

    maze = Maze(cellN)
    DFS = DFSSolver(maze.getBoard(), cellN)
    game = Game(window_width, window_height, maze, DFS)
    
    # Start the game
    game.start()

if __name__ == "__main__":
    main()
