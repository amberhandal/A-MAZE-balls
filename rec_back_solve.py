#!/usr/bin/env python3

# This program solves a maze using recursive backtracking.

import numpy as np
from maze.maze import Maze, MazeSymbols
from robot import Robot

maze = Maze.from_prims(100, 100)

# Constants used in this program:
WALL = MazeSymbols.WALL
EMPTY = MazeSymbols.EMPTY
START = MazeSymbols.START
GOAL = MazeSymbols.GOAL
PATH: str = '.'

# Get the height and width of the maze.
HEIGHT = maze.height
WIDTH = maze.width

def find_start(maze):
    """Pulls in the maze file and finds the start."""
    # Find the start position of the robot
    xx = 0
    for row in maze:
        yy = 0
        for element in row:
            if element == START:
                x_start, y_start = xx,yy
            yy +=1
        xx += 1

    print(f"Robot starting position: ({x_start},{y_start})")
    return x_start, y_start

############################### Beign_Citation [1, mazeSolver.py] ###############################
def solve_maze(maze, x=None, y=None, visited=None):
    """Solves the maze using recursive backtracking"""
    if x == None or y == None:
        x, y = maze.start_position[1], maze.start_position[0]
        maze.grid[y][x] = EMPTY
    if visited == None:
        visited = []

    if maze.grid[y][x] == GOAL:
        return True

    maze.grid[y][x] = PATH
    visited.append(str(x) + ',' + str(y))

    # Check the north position
    if y + 1 < HEIGHT and maze.grid[y + 1][x] in (EMPTY, GOAL) and \
    str(x) + ',' + str(y + 1) not in visited:
        if solve_maze(maze, x, y + 1, visited):
            return True
    # Check the south position
    if y - 1 >= 0 and maze.grid[y - 1][x] in (EMPTY, GOAL) and \
    str(x) + ',' + str(y - 1) not in visited:
        if solve_maze(maze, x, y - 1, visited):
            return True
    # Check the east position
    if x + 1 < WIDTH and maze.grid[y][x + 1] in (EMPTY, GOAL) and \
    str(x + 1) + ',' + str(y) not in visited:
        if solve_maze(maze, x + 1,y, visited):
            return True
    # Check the west position
    if x - 1 >= 0 and maze.grid[y][x - 1] in (EMPTY, GOAL) and \
    str(x - 1) + ',' + str(y) not in visited:
        if solve_maze(maze, x - 1, y, visited):
            return True

    maze.grid[y][x] = EMPTY
    
    return False
############################### End_Citation [1] ###############################

def main():
    """Initiates the solving algorithm."""
    print(maze)
    print("\n\n")
    solve_maze(maze)
    print(maze)

if __name__ == "__main__":
    main()