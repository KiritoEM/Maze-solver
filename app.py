from views.Game import Game
from models.DFSSolver import DFSSolver
from models.BFSSolver import BFSSolver
from models.Maze import Maze
import pygame

def main():
    window_width = 850
    window_height = 700
    cellN = 15

    maze = Maze(cellN) # Labyrinth class
    dfs = DFSSolver(maze.get_maze(), cellN) #DFS solver class
    bfs = BFSSolver(maze.get_maze(), cellN) #DFS solver class
    game = Game(window_width, window_height, maze, bfs) # New game
    
    # Start the game
    try:
        game.start()
    except KeyboardInterrupt:
        print("Game interrupted! Exiting...")
    pygame.quit()


if __name__ == "__main__":
    main()
