import numpy as np

class Belief_Status():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tot = 0
<<<<<<< HEAD
        self.old_loc = np.empty((h, w), dtype=int)
        self.loc = np.empty((h, w), dtype=int)

=======
        self.loc = np.empty((h, w), dtype=int)
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
    def set_locations(self, maze):
        for i in range(self.h):
            for j in range(self.w):
                if maze[i][j] != "#":
                    self.loc[i][j] = 1
                    self.tot += 1
                else:
                    self.loc[i][j] = 0
    
    def new_move(self, maze, dir):
<<<<<<< HEAD
        self.old_loc = self.loc.copy()
=======
        
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
        for i in range(self.h):
            for j in range(self.w):
                if self.loc[i][j] == 1 or self.loc[i][j] == 12:
                    if self.check_viable(dir, maze, i, j):
                        self.update_avail(dir, i, j)
                    else:
                        self.update_no(dir, i, j)
        self.update_total()
    
    def update_total(self):
<<<<<<< HEAD
        new_tot = 0
=======
        self.tot = 0
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
        for i in range(self.h):
            for j in range(self.w):
                if self.loc[i][j] > 1:
                    self.loc[i][j] = 1
<<<<<<< HEAD
                    new_tot += 1
                elif self.loc[i][j] == 1:
                    new_tot += 1   
        print(self.loc)
        if new_tot >= self.tot:
            self.loc = self.old_loc.copy()
        else:
            self.tot = new_tot

=======
                    self.tot += 1
                elif self.loc[i][j] == 1:
                    self.tot += 1   
        print(self.loc)     
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
    
    def check_viable(self, dir, maze, x, y):
        if dir == 0:
            tmp = maze[x+1][y]
            if tmp != '#':
                return True
            else:
                return False
        elif dir == 1:
            tmp = maze[x][y+1]
            if tmp != '#': 
                return True
            else:
                return False
        elif dir == 2:
            tmp = maze[x-1][y]
            if tmp != '#':
                return True
            else:
                return False
        else:
            tmp = maze[x][y-1]
            if tmp != '#': 
                return True
            else:
                return False

    def update_avail(self, dir, x, y):
        if dir == 0:
            if self.loc[x+1][y] == 1:
                self.loc[x+1][y] = 12
            else:
                self.loc[x+1][y] = 2

<<<<<<< HEAD
            if self.loc[x][y] <= 1:
=======
            if (self.loc[x][y] <= 1):
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
                self.loc[x][y] = 0
            
        elif dir == 1:
            if self.loc[x][y+1] == 1:
                self.loc[x][y+1] = 12
            else:
                self.loc[x][y+1] = 2
                
<<<<<<< HEAD
            if self.loc[x][y] <= 1:
=======
            if (self.loc[x][y] <= 1):
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
                self.loc[x][y] = 0
        elif dir == 2:
            if self.loc[x-1][y] == 1:
                self.loc[x-1][y] = 12
            else:
                self.loc[x-1][y] = 2

<<<<<<< HEAD
            if self.loc[x][y] <= 1:
=======
            if (self.loc[x][y] <= 1):
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
                self.loc[x][y] = 0
        else:
            if self.loc[x][y-1] == 1:
                self.loc[x][y-1] = 12
            else:
                self.loc[x][y-1] = 2

<<<<<<< HEAD
            if self.loc[x][y] <= 1:
=======
            if (self.loc[x][y] <= 1):
>>>>>>> 2fb9655 (Moved Belief_Status class to a new file)
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
