#!usr/bin/env python3
import numpy as np
from robot import Robot
from belief import Belief_Status
# import Maze

maze_name = "default-maze.txt"



# def belief():

def main():
    w = 10
    h = 10
    goal = np.array([0, 0])
    start = np.array([0, 0]) 
    maze = np.empty((h, w), dtype=str)
    
    with open(maze_name) as f:
        i = 0
        for x in f:
            for j in range(len(x)-1):
                maze[i][j] = x[j]
                if x[j] == 'R':
                    start[0] = i
                    start[1] = j
                if x[j] == 'G':
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