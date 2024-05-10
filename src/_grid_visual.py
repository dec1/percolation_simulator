from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches

from typing import List, Tuple
from src._grid import Grid
from src._cell import Cell
# -------------------------------------
def visualize_grid_sequence(num_rows: int, num_cols: int, sequence: List[Tuple[int,int]]):
    """
    Visualizes the order of cells in the sequence, using a color map.
    """

    # Create a grid initialized to NaN values
    grid = np.full((num_rows, num_cols), np.nan)

    # Fill the grid with indices reflecting the sequence order
    for order, (row, col) in enumerate(sequence):
        grid[row, col] = order

    # Normalize the sequence order to [0, 1] for color mapping
    normalized = grid / np.nanmax(grid)

    # Create a colormap (red to blue)
    colormap = mcolors.LinearSegmentedColormap.from_list("", ["red", "blue"])

    # Plot the grid
    plt.imshow(normalized, cmap=colormap, interpolation='nearest')

    # Loop to overlay sequence numbers
    for order, (row, col) in enumerate(sequence):
        # Use plt.text() to put the sequence number in each cell
        # Adjust the text color ("black" or "white") based on the cell's background color for readability
        text_color = "white" if normalized[row, col] < 0.5 else "black"
        plt.text(col, row, str(order), color=text_color, ha="center", va="center")


    # Optionally, add a colorbar to indicate the sequence order
    plt.colorbar(label='Sequence Order')

    plt.title('Grid Sequence Visualization')
    plt.xlabel('Column Index')
    plt.ylabel('Row Index')
    plt.show()

# -------------------------------------
def plot_grid_with_adjacent(num_rows, num_cols, row_idx, col_idx, adjacent_cells : List[Tuple[int, int]]):

    """
    Visualizes the grid of size (num_rows x num_cols) with cell at (row_idx, col_idx) and adjacent_cells
    using a color map.
    """

    grid = np.full((num_rows, num_cols, 3), 255)  # Start with an all-white grid

    # Color the original cell blue
    grid[row_idx, col_idx] = [0, 0, 255]

    # Color the adjacent cells yellow
    for r, c in adjacent_cells:
        grid[r, c] = [255, 255, 0]

    # Display the grid
    plt.imshow(grid.astype('uint8'), aspect='equal')

    # Add grid lines
    plt.grid(which='major', axis='both', linestyle='-', color='black', linewidth=2)
    plt.xticks(np.arange(-0.5, num_cols, 1))
    plt.yticks(np.arange(-0.5, num_rows, 1))

    # Hide tick labels
    plt.tick_params(axis='both', which='both', length=0, labelbottom=False, labelleft=False)

    plt.show()
# -------------------------------------
def visualize_grid_clusters(grid: Grid):

        def color_cell(ax, cell: Cell, color):
            # Assuming cell has row and col attributes
            rect = patches.Rectangle((cell.col_idx, cell.row_idx), 1, 1, linewidth=0, edgecolor='black', facecolor=color)
            ax.add_patch(rect)


        # Initialize a white grid
        fig, ax = plt.subplots()
        ax.set_xlim(0, grid.num_cols)
        ax.set_ylim(0, grid.num_rows)
        ax.invert_yaxis()  # Invert y axis to have origin at top-left

        # Color mapping
        for cluster in grid.clusters:
            for cell in cluster.cells:
                color = 'yellow' if cluster == grid.perc_cluster else 'blue'
                if cell == grid.perc_cell:
                    color = 'green'
                color_cell(ax, cell, color)

        # Non-cluster cells, assuming you have a way to determine these, are colored white by default

        # Draw grid lines
        for x in range(grid.num_cols):
            for y in range(grid.num_rows):
                rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='black', facecolor='none')
                ax.add_patch(rect)

        # Show steps taken
        plt.text(0, -1, f'Steps taken: {grid.steps_taken}', fontsize=12)

        plt.axis('off')
        plt.show()
# -------------------------
def visualize_as_histogram(ps:List[float], x_label: str = "Value", title: str = 'Histogram of p values'):
    #counts, bins = np.histogram(ps)
    #plt.stairs(counts, bins)

    plt.hist(ps, bins='auto')
    #plt.hist(ps, bins=100)  # 'auto' lets matplotlib decide the number of bins
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel('Frequency')
    plt.show()
