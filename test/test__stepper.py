""" Stepper tests """

from src._stepper import Stepper
from src._grid_visual import visualize_grid_sequence, visualize_grid_clusters
from src._config import Config
# --------------------------------------------
def test_stepper(want_visualize: bool = Config.want_plots()):
    """ Run an experiment """
    num_rows = 3
    num_cols = 3



    seq = [(2, 0), (2, 2), (1, 1), (1, 0), (2, 1), (0, 2), (0, 0), (1, 2), (0, 1)]

    if want_visualize:
        visualize_grid_sequence(num_rows, num_cols, seq)

    stepper = Stepper(num_rows, num_cols)
    stepper.do_steps(seq)

    if want_visualize:
        grid = stepper.grid
        visualize_grid_clusters(grid)


# --------------------------------------------
