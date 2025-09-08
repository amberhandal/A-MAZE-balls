#!/usr/bin/env python3

# This program solves a maze using recursive backtracking.

import numpy as np
# from maze import Maze
from robot import Robot

# from pathlib import Path

def open_maze():
    """Pulls in the maze file and finds the start."""
    maze = np.array([['#','#','#','#','#','#'],
                    ['#','R','#','#','#','#'],
                    ['#',' ',' ',' ','G','#'],
                    ['#','#','#','#','#','#']])
    # print(maze)
    xx = 0
    for row in maze:
        yy = 0
        for element in row:
            #print(f"({xx},{yy}) ")
            if element == 'R':
                x_start, y_start = xx,yy
            yy +=1
        xx += 1

    print(f"Robot starting position: ({x_start},{y_start})")
    return x_start, y_start


def main():
    """Initiates the solving algorithm."""
    x_start, y_start = open_maze()
    robinator3000 = Robot(x_start,y_start, False)
    print(robinator3000.x)

if __name__ == "__main__":
    main()