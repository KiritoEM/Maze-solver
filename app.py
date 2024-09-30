from views.Game import Game
from models.DFSSolver import DFSSolver
from models.Maze import Maze

def main():
    window_width = 850
    window_height = 700
    cellRows = 17
    cellCols = 21 

    maze = Maze(cellRows, 21)
    DFS = DFSSolver(maze.getBoard(), cellRows, cellCols)
    game = Game(window_width, window_height, maze, DFS)
    
    # Start the game
    game.start()

if __name__ == "__main__":
    main()
