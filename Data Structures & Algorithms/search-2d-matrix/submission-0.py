class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
modify binary search for 1-D arrays for 2-D array 

brute force approach
traverse through rows and columns 
at any point check if value at row and column is equal to target 
return true 
else return false 
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        '''
        #rows, cols = len(matrix), len(matrix[0])
        for r in range(len(matrix)): # 0, 1, 2, 3
            for c in range(len(matrix[0])): # 0, 1, 2, 3
                if matrix[r][c] == target:
                    return True 
        return False 