from __future__ import annotations

from typing import Optional

# keep mypy happy, without actually importing (and thereby creating circular dependency  cluster <-> cell)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ._grid import Grid
    from ._cluster import Cluster



class Cell:
    """ Smallest individual 'unit' of a grid. Has indices (x,y) and color"""

    # -------------------------------
    def __init__(self, row_idx: int, col_idx: int, is_black: bool = False, grid: Optional[Grid] = None):
        """ order of indices: (row_idx, col_idx) -not- (col_idx, row_idx)~(x,y)
           same convention as numpy/pandas """

        self.col_idx:  int  = col_idx
        self.row_idx:  int  = row_idx
        self.is_black: bool = is_black

        self.grid: Optional[Grid] = grid
        self.cluster: Optional[Cluster] = None


    # -------------------------------
    def turn_black(self, on=True):
        self.is_black = on
