from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        
        def is_boundary(row, col):
            return row >= 0 and col >= 0 and row < m and col < n
        
        def is_up(row, col):
            return (row + col) % 2 == 0
        
        res = []
        
        row = col = 0
        
        for i in range(m * n):
            res.append(mat[row][col])
            
            if is_up(row, col):
                if is_boundary(row - 1, col + 1):
                    row -= 1
                    col += 1
                elif is_boundary(row, col + 1):
                    col += 1
                else:
                    row += 1  
            else:
                if is_boundary(row + 1, col - 1):
                    row += 1
                    col -= 1
                elif is_boundary(row + 1, col):
                    row += 1
                else:
                    col += 1  
            
        return res
            

test = Solution()

assert test.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]