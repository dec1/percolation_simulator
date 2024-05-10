# Algorithm

The code uses the following algorithm.

- initialize:
    - set color of all cells to white (no clusters)
    - i =0 (cell number we are turning black) 
####
  - step i:
      - turn one of the white cells black
      - create new (size 1) cluster from this cell
      - for each adjacent black cell :
          - merge the clusters (remembering to tell each cell involved its new cluster):
            
                this is quite fast since:
                a) there are only 8 adjacent cells, to look at
                b) the cell can give you the cluster it is in - no computation required
                c) merging 2 clusters is fast - just combine the cells 
            
        - check do we have percolation now?
            - ie a single cluster that touches both top and bottom of grid:
    
                  this can be made quite fast too by clever storage of cells in cluster eg:
                    as a list of lists where each element of outer list is a row (in y order) and each
                    element of inner list is a cell (in x order) of the row
                    - they looking up left,right, top, bottom of cluster is fast: 
                       - top/bottom will always be y of any cell in first/last row 
                       - right/left will be min/max x of each first/last cell in rows

        - if percolation:
            - finished
            - **p = i/(rows x cols)** 
        - else:
            - next step (i -> i+1)
