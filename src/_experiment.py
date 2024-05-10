
from ._stepper import Stepper
from ._cell_picker import CellPicker
from ._grid_visual import visualize_grid_clusters, visualize_grid_sequence
from typing import List, Tuple, Optional


class Experiment:
    """  Create a grid and find percolation threshold, with visualization """

    def do_it(self, num_rows: int = 5, num_cols: int = 6, want_vis_seq : bool = False, want_vis_clusters : bool = False) -> int :

        stepper = Stepper(num_rows, num_cols)
        seq = CellPicker(num_rows, num_cols).seq_random()

        if want_vis_seq:
            visualize_grid_sequence(num_rows, num_cols, seq)

        stepper.do_steps(seq)
        grid = stepper.grid
        if (grid is None):
            print("...empty grid in experiment??")
            return -1

        if want_vis_clusters:
            visualize_grid_clusters(grid)

        p = grid.perc_value()
        print(f"...perc_value = {p}")
        return p

    # -------------------------------
