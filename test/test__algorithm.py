""" Algorithm tests """
from src._config import Config
from src._grid import Grid
from src._cell_picker import CellPicker
from src._grid_visual import visualize_grid_sequence
# --------------------------------------------
def test_cell_picker_seq_random(want_visualize: bool = Config.want_plots()):
    """ visualize cell picker sequence """

    num_rows = 5
    num_cols = 6
    picker = CellPicker(num_rows, num_cols)
    seq = picker.seq_random(deterministic=False)

    uniq_vals = set(seq)
    uniq_cnt = len(uniq_vals)
    assert uniq_cnt == (num_rows * num_cols), "expect all values chosen exactly once"

    seq_orig = [(row, col) for row in range(num_rows) for col in range(num_cols)]

    # Count the differences between the original and shuffled sequences
    num_differ = sum(1 for orig, shuffled in zip(seq, seq_orig) if orig != shuffled)
    assert num_differ > 0 , "expect shuffled sequence to differ from original"

    # plot the sequence in colors representing sequence order
    if want_visualize:
        visualize_grid_sequence(num_rows, num_cols, seq)
# --------------------------------------------


def test_cell_stepper():
    """ turn cells black in random order """

    num_rows = 5
    num_cols = 6
    grid = Grid(num_rows, num_cols)
    seq = CellPicker(num_rows, num_cols).seq_random()

    for (row_idx, col_idx) in seq:
        cell = grid.cell_at(row_idx, col_idx)
        cell.turn_black()
