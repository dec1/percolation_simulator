# Actors
- ### Grid 
     - Matrix of size (rows x cols).
     - Each element of the matrix is a cell.  

- ### Cell
    - **(x,y)**:  in grid  
      - 0 <= x < cols 
      - 0 <= y < rows 
    - **color** (black or white)
    - **cluster** this cell belongs to 
      - black cells are in exactly 1 cluster (possibly of size 1)
      - white cells are in 0 clusters
      
    - #### Terminology:
      - Cells are
        -  **Adjacent** 
            -  if they share an (vertical or horizontal) edge 
            - sharing a vertex is not sufficient
            - independent of color
    
        - **Connected**
          - _Intuitive_:
            - in Island of same color
          - _Rigorous_:
              - (c1,c2) are connected if there exists a sequence of cells starting with c1 and ending with c2, such that:
                - all cells in the sequence are same color, and
                - each pair of consecutive cells in the sequence are adjacent 

- ### Cluster
    - **Connected black** cells of **maximal** size 
        - _Intuitive_:
            - Full islands (not subsets thereof) of black
        - _Rigorous_:  
            - There is no cell not in the (black)  cluster that is connected to any cell that is
    - **size** of a cluster is the number of cells in the cluster.

- ### Percolation
    - Occurs when a single cluster touches both top and bottom of the grid.

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
                a) there are only (max) 4 adjacent cells, to look at
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
- ### Challenge
    If one (randomly chosen white) cell at a time is turned black, find the smallest proportion of cells that have 
    to be turned black in order for percolation to occur


        ...perc_value = 0.600475
        ...perc_value = 0.5849
        ...perc_value = 0.59185
        ...perc_value = 0.58535
        ...perc_value = 0.58995
        ...perc_value = 0.586175
        ...perc_value = 0.5989
        ...perc_value = 0.590425
        ...perc_value = 0.574925
        ...perc_value = 0.623675
        ...perc_value = 0.583475
        ...average p: 0.5917819999999999 with (200x200) grid, 50 iterations in 38.44 secs 
