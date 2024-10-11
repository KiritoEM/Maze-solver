from views.Game import Game
from models.DFSSolver import DFSSolver
from models.BFSSolver import BFSSolver
from models.Maze import Maze
import pygame

def main():
    window_width = 850
    window_height = 700
    cellN = int(input("Enter the number of maze grid cell: "))
    choice = input("DFS ou BFS ?  ")

    maze = Maze(cellN) 
    dfs = DFSSolver(maze.get_maze(),cellN) #DFS solver class
    bfs = BFSSolver(maze.get_maze(), cellN) #DFS solver class

    if choice == "DFS":
        game = Game(window_width, window_height,maze, dfs) # New game with DFS
    elif choice == "BFS":
        game = Game(window_width, window_height,maze, bfs) # New game with BFS
    
    # Start the game
    try:
        game.start()
    except KeyboardInterrupt:
        print("Game interrupted! Exiting...")
    pygame.quit()


if __name__ == "__main__":
    main()
