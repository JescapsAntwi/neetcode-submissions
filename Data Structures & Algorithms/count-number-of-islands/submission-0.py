class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        #matrix dfs and bfs 
        #every dfs call represents an island 
        # we mark 1s that we have visited as 0 to prevent looping recursion

        #each pair of directions represent a change in the column and row values 
        # row goes up when the index is decreased [-1,0], column stays the same
        #row goes down when the index is increased [1, 0]
        # column goes right when the index is increased [0, 1], row stays the same
        # column goes left when the index is decreased [0, -1]
        def dfs(r, c):
            if(r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return 
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands

