class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow 
        return row[0]



'''
3 x 6
compute the number of ways to reach the destination for each square. 
if we can do this, then we can do the same for the 'Start' square. 
every square (number of ways to reach the start) = right square value + square value below it
'''