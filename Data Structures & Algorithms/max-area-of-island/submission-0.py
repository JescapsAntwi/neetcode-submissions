class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        #directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]!=1):
                return 0
            grid[r][c] = 0

            size = 1
            size += dfs(r + 1, c)
            size += dfs(r - 1, c)
            size += dfs(r , c + 1)
            size += dfs(r, c - 1)

            return size 
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_size = dfs(r, c)
                    count = max(count, current_size)
        return count 
                    
