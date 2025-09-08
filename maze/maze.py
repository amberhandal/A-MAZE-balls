# manual maze generation for robot simulation using ascii art
# "#" represents walls, " " represents non-wall spaces, "R" represents the robot's starting position, "G" represents the goal position

from dataclasses import dataclass
from typing import List, Tuple, Optional
import json
import numpy as np

Pos = Tuple[int, int]

@dataclass(frozen=True)
class MazeSymbols:
    WALL: str = '#'
    EMPTY: str = ' '
    START: str = 'R'
    GOAL: str = 'G'

class Maze:
    def __init__(self, grid: np.ndarray | List[str], symbols: MazeSymbols = MazeSymbols()) -> None:
        self.symbols = symbols
        if isinstance(grid, list):
            self.grid = np.array([list(row) for row in grid])
        else:
            self.grid = grid

        self.height, self.width = self.grid.shape

        self._start_pos = self._find_position(self.symbols.START)
        self._goal_pos = self._find_position(self.symbols.GOAL)

        if self._start_pos:
            self.grid[self._start_pos] = self.symbols.EMPTY

    def __str__(self) -> str:
        display_grid = self.grid.copy()
        if self._start_pos:
            display_grid[self._start_pos] = self.symbols.START
        if self._goal_pos:
            display_grid[self._goal_pos] = self.symbols.GOAL
        return '\n'.join(''.join(row) for row in display_grid)

    def _find_position(self, symbol: str) -> Optional[Pos]:
        positions = np.where(self.grid == symbol)
        if len(positions[0]) > 0:
            return (int(positions[0][0]), int(positions[1][0]))
        return None

    @property
    def start_position(self) -> Optional[Pos]:
        return self._start_pos

    @property
    def goal_position(self) -> Optional[Pos]:
        return self._goal_pos

    @staticmethod
    def from_json(file_path: str, maze_key: str = 'DEFAULT_MAZE') -> 'Maze':
        with open(file_path, 'r') as f:
            data = json.load(f)
            if maze_key not in data:
                raise KeyError(f"Maze key '{maze_key}' not found in template file")
            return Maze(data[maze_key]['grid'])