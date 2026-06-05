class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
modify binary search for 1-D arrays for 2-D array (optimal approach)
- one pass

second approach 
staircase search 

brute force approach
traverse through rows and columns 
at any point check if value at row and column is equal to target 
return true 
else return false 
[[1, 2, 3], [4, 5, 6], [7, 8, 9]], target = 5

iteration 1, r = 0, c = 0, 1, 2
matrix[0][0] = 1 != 5
matrix[0][1] = 2 != 5 
matrix[0][2] = 3 != 5

iteration 2, r = 1, c = 0, 1, 2
matrix[1][0] = 4 != 5
matrix[1][1] = 5, return True 

time: O(n^2)
space: O(1)
 #rows, cols = len(matrix), len(matrix[0])
        for r in range(len(matrix)): # 0, 1, 2, 3
            for c in range(len(matrix[0])): # 0, 1, 2, 3
                if matrix[r][c] == target:
                    return True 
        return False 
        '''
        # staircase search 
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1

        while r < rows and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True 
        return False 
       