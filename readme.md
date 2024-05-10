## Actors
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

- ### Challenge
    If one (randonly chosen white) cell at a time is turned black, find the smallest proportion of cells that have 
    to be turned black in order for percolation to occur
