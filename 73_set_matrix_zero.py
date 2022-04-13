class Solution:
    """
        O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row_zero = False
        first_col_zero = False
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
                    if i == 0:
                        first_row_zero = True
                    
                    if j == 0:
                        first_col_zero = True
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row_zero:
            for i in range(cols):
                matrix[0][i] = 0
        
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
                    
    
    """
        O(n + m)
    """
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_rows = [False] * rows
        zero_cols = [False] * cols
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows[i] = True
                    zero_cols[j] = True
        
        for i in range(rows):
            for j in range(cols):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0
        
    """
        O(n*m) solution
    """
    def setZeroes3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
                    
        for x, y in zeros:
            for i in range(rows):
                matrix[i][y] = 0
            
            for j in range(cols):
                matrix[x][j] = 0
                
        