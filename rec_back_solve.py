#!/usr/bin/env python3

# This program solves a maze using recursive backtracking.

import numpy as np
import maze
import robot

from pathlib import Path

def open_maze():
    """Pulls in the maze file and finds the start."""
    # path = Path('test-maze.txt')
    # contents = path.read_text()
    # lines = contents.splitlines()
    # for line in lines:
    #     print(line)

    np.array([['#','#','#','#','#','#'],
              ['#','R','#','#','#','#'],
              ['#',' ',' ',' ','G','#'],
              ['#','#','#','#','#','#']])

def main():
    """Initiates the solving algorithm."""
    open_maze()

if __name__ == "__main__":
    main()