from views.Game import Game
from models.DFSSolver import DFSSolver
from models.Maze import Maze
import pygame

def main():
    window_width = 850
    window_height = 700
    cellN = 31

    maze = Maze(cellN)
    DFS = DFSSolver(maze.getBoard(), cellN)
    game = Game(window_width, window_height, maze, DFS)
    
    # Start the game
    try:
        game.start()
    except KeyboardInterrupt:
        print("Game interrupted! Exiting...")
    pygame.quit()


if __name__ == "__main__":
    main()
