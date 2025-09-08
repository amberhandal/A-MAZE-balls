#!usr/bin/env python3
import numpy as np
from robot import Robot
# import Maze

maze_name = "test-maze.txt"

Class Belief_Status():
    def __init__(self, w, h, tot):
        self.w = w
        self.h = h
        self.tot = tot
        self.loc = numpy.empty((h, w), dtype=int)

    def set_locations(self, maze):
        for i in len(maze):
            for j in len(maze[i])
                if maze[i][j] == ' ' or maze[i][j] == 'R' or maze[i][j] == 'G':
                    loc[i][j] = 1
                    tot += 1
                else
                    loc[i][j] = 0
    
    def new_move(self, maze):
        z = 0
        for i in range(h):
            for j in range(w):
                if (loc == 1):
                    if check_viable(z, maze, i, j):
                        update_avail(z, x, y)
                    else:
                        update_no(z, x, y)

                
    
    def check_viable(self, dir, maze, x, y):
        if dir == 0:
            tmp = maze[x+1][y]
            if tmp == ' ' or tmp == 'R' or tmp == 'G':
                return True
            else:
                return False
        elif dir == 1:
            tmp = maze[x][y+1]
            if tmp == ' ' or tmp == 'R' or tmp == 'G': 
                return True
            else:
                return False
        elif dir == 2:
            tmp = maze[x-1][y]
            if tmp == ' ' or tmp == 'R' or tmp == 'G': 
                return True
            else:
                return False
        else:
            tmp = maze[x][y-1]
            if tmp == ' ' or tmp == 'R' or tmp == 'G': 
                return True
            else:
                return False

    def update_avail(self, dir, x, y):
        if dir == 0:
            loc[x+1][y] = 1
            loc[x][y] = 0
        elif dir == 1:
            loc[x][y+1] = 1
            loc[x][y] = 0
        elif dir == 2:
            loc[x-1][y] = 1
            loc[x][y] = 0
        else:
            loc[x][y-1] = 1
            loc[x][y] = 0

    def update_no(self, dir, x, y):
        if dir == 0:
            loc[x+1][y] = 0
        elif dir == 1:
            loc[x][y+1] = 0
        elif dir == 2:
            loc[x-1][y] = 0
        else:
            loc[x][y-1] = 0


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