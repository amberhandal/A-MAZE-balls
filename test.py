from maze.maze import Maze

def main():
    print("LOAD DEFAULT MAZE:")
    default_maze = Maze.from_json('maze-templates.json', 'DEFAULT_MAZE')
    print(default_maze)
    print(f"Start pos: {default_maze.start_position}")
    print(f"Goal pos: {default_maze.goal_position}")

if __name__ == "__main__":
    main()