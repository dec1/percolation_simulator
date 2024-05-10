from __future__ import annotations

from typing import Set

# keep mypy happy, without actually importing (and thereby creating circular dependency  cluster <-> cell)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
        from ._grid import Grid
        from ._cell import Cell


class Cluster:
    """ Full islands (not subsets thereof) of black cells """



    # -------------------------------
    def __init__(self, grid: Grid):
        self.grid = grid

        self.cells: Set[Cell] = set()  # using set (instead of eg List) stops duplicates from being added (by mistake)

        # used to tell if cluster percolates
        self.row_idx_min: int = -1  # the closer to 0, the closer to top of grid
        self.row_idx_max: int = -1  # the closer to (grid.num_cols)-1, the closer to top of grid


    # -------------------------------
    def num_cells(self) -> int:
        return len(self.cells)

    # -------------------------------
    def percolates(self) -> bool:
        """ does cluster extend from top to bottom of grid? """
        if self.grid is None:
            return False

        touches_top = self.row_idx_min == 0
        touches_bottom = self.row_idx_max == (self.grid.num_rows-1)

        return touches_top and touches_bottom

    # -------------------------------
    def add_cell(self, cell: Cell):
        if (cell is not None) and (cell.is_black):
            self.cells.add(cell)
            self.update_col_idx(cell)
            cell.cluster = self

    # -------------------------------
    def update_col_idx(self, cell: Cell) -> None:
        """ updates col_idx_min/max if cell is closer to top/bottom of grid"""
        if cell is None:
            return

        if (self.row_idx_min <0) or (self.row_idx_min > cell.row_idx) :
            self.row_idx_min = cell.row_idx

        if (self.row_idx_max <0) or (self.row_idx_max < cell.row_idx) :
            self.row_idx_max = cell.row_idx

    # -------------------------------
    def merge(self, other: Cluster):
        """ merges other cluster into this cluster """

        if (other is None) or (other is self):
            return

        # add cells from other cluster
        for cell in other.cells:
            self.add_cell(cell)

        # reset other cluster
        other.row_idx_min = -1  # the closer to 0, the closer to top of grid
        other.row_idx_max = -1  # the closer to (grid.num_cols)-1, the closer to top of grid
        other.grid = None
        other.cells = set()
