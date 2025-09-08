# manual maze generation for robot simulation using ascii art
# "#" represents walls, " " represents non-wall spaces, "R" represents the robot's starting position, "G" represents the goal position

from dataclasses import dataclass
from typing import List, Tuple
import json
import numpy as np

Pos = Tuple[int, int]

@dataclass(frozen=True)
class MazeSymbols:
    WALL: str='#'
    EMPTY: str=' '
    START: str='R'
    GOAL: str='G'

class Maze:
    def __init__(self, grid: np.ndarray | List[str], symbols: MazeSymbols=MazeSymbols()) -> None:
        self.symbols = symbols
        if isinstance(grid, list):
            self.grid = np.array([list(row) for row in grid])
        else:
            self.grid = grid

        self.height, self.width = self.grid.shape

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self.grid)

    def to_json(self) -> str:
        return json.dumps(self.grid.tolist())

    @staticmethod
    def from_json(file_path: str, maze_key: str = 'DEFAULT_MAZE') -> 'Maze':
        with open(file_path, 'r') as f:
            data = json.load(f)
            if maze_key not in data:
                raise KeyError(f"Maze key '{maze_key}' not found in template file")
            return Maze(data[maze_key]['grid'])