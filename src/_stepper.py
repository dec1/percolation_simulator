from __future__ import annotations

from ._grid import Grid
from typing import List, Tuple, Optional


class Stepper:
    """  Given dims of grid (num_rows x num_cols)  and a sequences of cells, turn them black, merge any clusters. """

    num_rows: int = -1
    num_cols: int = -1
    grid: Optional[Grid] = None

    # -------------------------------
    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = Grid(num_rows, num_cols)

    # -------------------------------
    def do_steps(self, indices: List[Tuple[int, int]]) -> bool:

        if (indices is None) or (self.grid is None):
            return False

        for (row_idx, col_idx) in indices:
            percolates = self.grid.step(row_idx, col_idx)
            if percolates:
                cluster = self.grid.perc_cluster
                cell = self.grid.perc_cell
                steps = self.grid.steps_taken
                # print(f"Percolated at step {steps} of {self.num_rows * self.num_cols} in cluster {cluster} at cell {cell}")
                return True

        print(f"No Percolation occurred ...")
        return False

    # -------------------------------
