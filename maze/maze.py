# manual maze generation for robot simulation using ascii art
# "█"represents walls, " " represents non-wall spaces, "R" represents the robot's starting position, "G" represents the goal position
# TODO: refactor
# TODO: add citations
# TODO: start pos and goal pos should be a min distance from eachother
from dataclasses import dataclass
from typing import List, Tuple, Optional
import json
import numpy as np
import random

Pos = Tuple[int, int]

############################### Begin_Citation [3] ############################
@dataclass
class MazeSymbols:
    WALL: str = '█'
    EMPTY: str = ' '
    START: str = 'R'
    GOAL: str = 'G'
############################### End_Citation [3]  #############################

class Maze:
    ############################### Begin_Citation [4] ############################
    # Creation from list -> ndarray, dtype as unicode scalars, and shape handling are
    # guided by NumPy ndarray semantics and documentation.
    def __init__(self, grid: np.ndarray | List[str], symbols: MazeSymbols = MazeSymbols()) -> None:
        self.symbols = symbols
        if isinstance(grid, list):
            self.grid = np.array([list(row) for row in grid])
        else:
            self.grid = grid

        self.height, self.width = self.grid.shape
    ############################### End_Citation [4] #############################

        ############################### Begin_Citation [5] ############################
        # Use of Optional[Pos] for possibly-absent start/goal positions is aligned with typing docs.
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
    ############################### End_Citation [5]  ############################

    @staticmethod
    def from_json(file_path: str, maze_key: str = 'DEFAULT_MAZE') -> 'Maze':
        with open(file_path, 'r') as f:
            data = json.load(f)
            if maze_key not in data:
                raise KeyError(f"Maze key '{maze_key}' not found in template file")
            return Maze(data[maze_key]['grid'])

    ############################### Begin_Citation [6] ############################
    # The structure of this generator (frontier expansion, carve if exactly one adjacent empty,
    # 4-neighborhood) is adapted from Jamis Buck's description of Prim's algorithm for mazes.
    @staticmethod
    def from_prims(width: int, height: int) -> 'Maze':
        WALL = MazeSymbols.WALL
        EMPTY = MazeSymbols.EMPTY
        START = MazeSymbols.START
        GOAL = MazeSymbols.GOAL

        # all cells are walls initially
        grid = [[WALL for _ in range(width)] for _ in range(height)]

        def in_bounds(row: int, col: int) -> bool:
            return 1 <= row < height-1 and 1 <= col < width-1

        def adjacent_cells(row: int, col: int):
            for r, c in [(-1,0), (1,0), (0,-1), (0,1)]:
                next_row, next_col = row + r, col + c
                if in_bounds(next_row, next_col):
                    yield next_row, next_col

        # start generation away from borders
        row = random.randint(1, height - 2)
        col = random.randint(1, width - 2)
        grid[row][col] = EMPTY

        ############################### Begin_Citation [7] ############################
        # Use of a set for the frontier collection and add/remove operations.
        frontier = set()
        for next_row, next_col in adjacent_cells(row, col):
            if grid[next_row][next_col] == WALL:
                frontier.add((next_row, next_col))
        ############################### End_Citation [7]  #############################

        while frontier:
            next_cell = random.choice(tuple(frontier))
            frontier.remove(next_cell)
            next_row, next_col = next_cell

            empty_count = 0
            for adjacent_row, adjacent_col in adjacent_cells(next_row, next_col):
                if grid[adjacent_row][adjacent_col] == EMPTY:
                    empty_count += 1

            if empty_count == 1:
                grid[next_row][next_col] = EMPTY
                for wall_row, wall_col in adjacent_cells(next_row, next_col):
                    if grid[wall_row][wall_col] == WALL:
                        frontier.add((wall_row, wall_col))

        empty_cells = [(row, col) for row in range(1, height-1) 
                      for col in range(1, width-1) 
                      if grid[row][col] == EMPTY]

        start_pos, goal_pos = random.sample(empty_cells, 2)
        grid[start_pos[0]][start_pos[1]] = START
        grid[goal_pos[0]][goal_pos[1]] = GOAL

        return Maze(grid)
    ############################### End_Citation [6]  #############################
