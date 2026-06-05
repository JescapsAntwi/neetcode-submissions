class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
my understanding:
you have a grid where each cell is -1, 0 or INF and these mean sth 
now for each INF in the grid, calculate the nearest distance to its nearest 0 and replace the INF 
value with the distance calculated and only do this, if the nearest 0 can be reached by traversing 
up, down, left, right. If this isn't possible, it should remain INF. 
All of this has to done in-place (no external data structure).

    3 3 3 3 
        3 3 3 3 

        2 x 4 
        '''
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def addCell(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return 
            visit.add((r, c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visit.add((r, c))
        
        # calculate the shortest distance from every land cell to the nearest treasure
        dist = 0 
        while queue: 
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist 
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1 



    