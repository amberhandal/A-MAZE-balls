from maze.maze import Maze

def main():
    print("Default Maze:")
    default_maze = Maze.from_json('maze-templates.json', 'DEFAULT_MAZE')
    print(default_maze)
    
    # print("Test Maze:")
    # test_maze = Maze.from_json('maze-templates.json', 'TEST_MAZE')
    # print(test_maze)

if __name__ == "__main__":
    main()