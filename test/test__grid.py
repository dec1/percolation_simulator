""" Grid tests """

from src._config import Config
from src._grid import Grid
from src._grid_visual import plot_grid_with_adjacent


# --------------------------------------------
def test_grid_create():
    """test grid creation()"""

    grid = Grid(num_rows=3, num_cols=3)

    assert grid.num_cols == 3, "num_cols is not 3"
    assert grid.num_rows == 3, "num_rows is not 3"
    # --------
    grid = Grid(num_rows=1, num_cols=3)

    assert grid.num_cols == 3, "num_cols is not 1"
    assert grid.num_rows == 1, "num_rows is not 3"
    # --------
    cell = grid.cell_at(0, 1)
    assert cell is not None, "grid cell is None"
    assert cell.row_idx == 0, "grid cell.row is not 0"
    assert cell.col_idx == 1, "grid cell.col is not 1"


# --------------------------------------------
def __test_adjacent_cells(
    num_rows, num_cols, row_idx, col_idx, expected_adj, mesg, want_visualize: bool = Config.want_plots()
):

    ret = Grid.indices_adjacent_to(num_rows, num_cols, row_idx, col_idx)
    assert ret == expected_adj, mesg

    if want_visualize:
        plot_grid_with_adjacent(num_rows, num_cols, row_idx, col_idx, ret)


# --------------------------------------------
def test_adjacent_cells_multiple():

    num_rows = 5
    num_cols = 6

    # Test: Corner case (Top-Left corner)
    __test_adjacent_cells(
        num_rows=num_rows,
        num_cols=num_cols,
        row_idx=0,
        col_idx=0,
        expected_adj=[
            (0, 1),
            (1, 0),
        ],
        mesg="Top-Left corner failed",
    )

    # Test: Corner case (Bottom-Right corner)
    __test_adjacent_cells(
        num_rows=num_rows,
        num_cols=num_cols,
        row_idx=4,
        col_idx=5,
        expected_adj=[(3, 5), (4, 4)],
        mesg="Bottom-Right corner failed",
    )

    # Test: Edge case (Top edge, not corner)
    assert Grid.indices_adjacent_to(num_rows, num_cols, 0, 2) == [(0, 1), (0, 3), (1, 2)], "Top edge failed"
    __test_adjacent_cells(
        num_rows=num_rows,
        num_cols=num_cols,
        row_idx=0,
        col_idx=2,
        expected_adj=[(0, 1), (0, 3), (1, 2)],
        mesg="Top edge failed",
    )

    # Test: Edge case (Left edge, not corner)
    __test_adjacent_cells(
        num_rows=num_rows,
        num_cols=num_cols,
        row_idx=2,
        col_idx=0,
        expected_adj=[(1, 0), (2, 1), (3, 0)],
        mesg="Left edge failed",
    )

    # Test: Center (Not an edge or corner)
    __test_adjacent_cells(
        num_rows, num_cols, row_idx=2, col_idx=2, expected_adj=[(1, 2), (2, 1), (2, 3), (3, 2)], mesg="Center failed"
    )
