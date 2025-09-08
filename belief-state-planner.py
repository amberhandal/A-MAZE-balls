#!usr/bin/env python3
import numpy as np
from robot import Robot
# import Maze

maze_name = "test-maze.txt"

class Belief_Status():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tot = 0
        self.loc = np.empty((h, w), dtype=int)

    def set_locations(self, maze):
        for i in range(self.h):
            for j in range(self.w):
                if maze[i][j] == ' ' or maze[i][j] == 'R' or maze[i][j] == 'G':
                    self.loc[i][j] = 1
                    self.tot += 1
                else:
                    self.loc[i][j] = 0
    
    def new_move(self, maze, dir):
        for i in range(self.h):
            for j in range(self.w):
                if (self.loc[i][j] == 1):
                    if self.check_viable(dir, maze, i, j):
                        self.update_avail(dir, i, j)
                    else:
                        self.update_no(dir, i, j)
        self.update_total()

    def update_total(self):
        self.tot = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.loc[i][j] == 1:
                    self.tot += 1        
    
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
            self.loc[x+1][y] = 1
            self.loc[x][y] = 0
        elif dir == 1:
            self.loc[x][y+1] = 1
            self.loc[x][y] = 0
        elif dir == 2:
            self.loc[x-1][y] = 1
            self.loc[x][y] = 0
        else:
            self.loc[x][y-1] = 1
            self.loc[x][y] = 0

    def update_no(self, dir, x, y):
        if dir == 0:
            self.loc[x+1][y] = 0
        elif dir == 1:
            self.loc[x][y+1] = 0
        elif dir == 2:
            self.loc[x-1][y] = 0
        else:
            self.loc[x][y-1] = 0

    def final_loc(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.loc[i][j] == 1:
                    return np.array([i, j])      


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

    lil_guy = Robot(start[0], start[1])
    loc = np.array([0, 0])
    robot_knows = Belief_Status(w, h)
    robot_knows.set_locations(maze)
    while True:
        for i in range(4):
            lil_guy.move(i, maze)
            tmp = robot_knows.tot
            robot_knows.new_move(maze, i)
            if robot_knows.tot < tmp:
                break
        if robot_knows.tot == 1:
            loc = robot_knows.final_loc()
            break
    
    print(lil_guy)
    print(loc)


if __name__ == "__main__":
    main()