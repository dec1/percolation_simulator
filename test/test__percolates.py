""" Percoaltes tests """

from src._grid import Grid
from src._cluster import Cluster
from src._cell import Cell
# --------------------------------------------
def test_grid_percolates():
    """ test cluster creation() """

    grid  = Grid(num_rows=3, num_cols=2)
    cluster = Cluster(grid=grid)

    cell_0_0 = Cell(0,0, is_black=True)
    cell_1_0 = Cell(1,0, is_black=True)


    cluster.add_cell(cell_0_0)
    assert not cluster.percolates(), "expect no cluster percolation"

    cluster.add_cell(cell_1_0)
    assert not cluster.percolates(), "expect no cluster percolation"

    cell_2_0 = Cell(2, 0, is_black=False)
    cluster.add_cell(cell_2_0)
    assert not cluster.percolates(), "expect no cluster percolation (added white cell)"


    cell_2_0 = Cell(2, 0, is_black=True)
    cluster.add_cell(cell_2_0)
    assert cluster.percolates(), ("expect cluster percolation (added black cell)")
