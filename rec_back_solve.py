#!/usr/bin/env python3

# This program solves a maze using recursive backtracking.

import numpy as np
# from maze import Maze
from robot import Robot

# from pathlib import Path

##########
#R###### #
# ###    #
# ##### ##
# ###   ##
# ##### G#
##########

maze = np.array([['#','#','#','#','#','#','#','#','#','#','#','#'],
                    ['#','R','#','#','#','#'],
                    ['#',' ',' ',' ','G','#'],
                    ['#','#','#','#','#','#']])

# Constants used in this program:
WALL: str = '#'
EMPTY: str = ' '
START: str = 'R'
GOAL: str = 'G'
PATH: str = '.'

# Get the height and width of the maze and find start location
HEIGHT = len(maze)
WIDTH = 0
for row in maze:
    if len(row) > WIDTH:
        WIDTH = len(row)

# Make each row in the maze a list as wide as the width
for ii in range(len(maze)):
    maze[ii] = list(maze[ii])
    if len(maze[ii]) != WIDTH:
        maze[ii] = [EMPTY] * WIDTH

def print_maze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(maze[y][x], end='')
        print()
    print()

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

def solve_maze(maze, x=None, y=None, visited=None):
    """Solves the maze using recursive backtracking"""
    if x == None or y == None:
        x, y = find_start(maze)
        maze[y][x] = EMPTY 
    if visited == None:
        visited = []

    if maze[y][x] == GOAL:
        return True

    maze[y][x] = PATH
    visited.append(str(x) + ',' + str(y))

    # Check the north position
    if y + 1 < HEIGHT and maze[y + 1][x] in (EMPTY, GOAL) and \
    str(x) + ',' + str(y + 1) not in visited:
        if solve_maze(maze, x, y + 1, visited):
            return True
    # Check the south position
    if y - 1 >= 0 and maze[y - 1][x] in (EMPTY, GOAL) and \
    str(x) + ',' + str(y - 1) not in visited:
        if solve_maze(maze, x, y - 1, visited):
            return True
    # Check the east position
    if x + 1 < WIDTH and maze[y][x + 1] in (EMPTY, GOAL) and \
    str(x + 1) + ',' + str(y) not in visited:
        if solve_maze(maze, x + 1,y, visited):
            return True
    # Check the west position
    if x - 1 >= 0 and maze[y][x - 1] in (EMPTY, GOAL) and \
    str(x - 1) + ',' + str(y) not in visited:
        if solve_maze(maze, x - 1, y, visited):
            return True
        
    maze[y][x] = EMPTY

    return False

def main():
    """Initiates the solving algorithm."""
    #x_start, y_start = find_start()
    #robotinator3000 = Robot(x_start,y_start, False)
    #print(robotinator3000.x)
    print_maze(maze)
    solve_maze(maze)
    print_maze(maze)

if __name__ == "__main__":
    main()