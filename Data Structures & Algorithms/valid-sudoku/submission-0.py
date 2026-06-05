class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row validity 
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": #board[2][i] value at row 3 of column i 
                    continue 
                if board[row][i] in seen:
                    return False 
                seen.add(board[row][i])
        
        #column validity 
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".": #board[i][2] values in column 3 of row i 
                    continue 
                if board[i][col] in seen:
                    return False 
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i  #for checking the starting row and columns of each sub box
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue 
                    if board[row][col] in seen:
                        return False 
                    seen.add(board[row][col])
        return True 
        
