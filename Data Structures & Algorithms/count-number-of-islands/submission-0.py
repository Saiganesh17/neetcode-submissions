class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row:int, col:int)->None:
            grid[row][col]='0'
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                next_row, next_col= row+dr, col+ dc
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    grid[next_row][next_col] == '1'):
                    # Recursively explore the adjacent land
                    dfs(next_row, next_col)
      
        # Initialize island counter
        island_count = 0
      
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
      
        # Traverse each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find unvisited land, it's a new island
                if grid[i][j] == '1':
                    # Explore and mark the entire island
                    dfs(i, j)
                    # Increment island count
                    island_count += 1
      
        return island_count
        #Time and space complexity is O(m* n) and O(m* n ) respectively 
        #where m is the no of rows and n is the number of columns in the grid 