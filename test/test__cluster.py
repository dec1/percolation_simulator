""" Cluster tests """

from src._cluster import Cluster
from src._cell import Cell
# --------------------------------------------
def test_grid_create():
    """ test cluster creation() """

    cluster = Cluster(grid=None)
    cell_1 = Cell(0,0, is_black=True)
    cell_2 = Cell(1,0, is_black=True)
    cell_3 = Cell(2, 0, is_black=False)

    cluster.add_cell(cell_1)
    assert cluster.num_cells() == 1, "expect 1 cell in cluster"

    cluster.add_cell(cell_2)
    assert cluster.num_cells() == 2, "expect 2 cells in cluster"

    cluster.add_cell(cell_2)
    assert cluster.num_cells() == 2, "expect not to add cell twice"

    cluster.add_cell(cell_3)
    assert cluster.num_cells() == 2, "expect not to add whote cell"
