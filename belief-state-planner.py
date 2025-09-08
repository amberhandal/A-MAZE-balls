#!usr/bin/env python3
import numpy as np
from robot import Robot
# import Maze

maze_name = "test-maze.txt"

# def belief():

def main():
    w = 6
    h = 4
    goal = np.array([0, 0])
    start = np.array([0, 0]) 
    maze = np.empty((h, w), dtype=str)
    with open(maze_name) as f:
        i = 0
        for x in f:
            for j in range(len(x)-1):
                maze[i][j] = x[j]
                if (x[j] == 'R'):
                    start[0] = i
                    start[1] = j
                if (x[j] == 'G'):
                    goal[0] = i
                    goal[1] = j
            i += 1

    for line in maze:
        for char in line:
            print(char, end=" ")
        print()

    lil_guy = Robot(start[0], start[1], False)

    # while true:
        


if __name__ == "__main__":
    main()