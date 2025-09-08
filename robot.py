class Robot():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isfinish = False

    def __str__(self):
        return f"I'm at {self.x} {self.y}. My state is {self.isfinish}. Bye Bye Silly Goose."
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dir, maze):
        if dir == 0:
            if maze[self.x+1][self.y] != '#':
                self.x += 1 
        elif dir == 1:
            if maze[self.x][self.y+1] != '#':
                self.y += 1
        elif dir == 2:
            if maze[self.x-1][self.y] != '#':
                self.x -= 1
        else:
            if maze[self.x][self.y-1] == '#':
                self.y -= 1

        