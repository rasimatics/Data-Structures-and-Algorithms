class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r-l):
                t, b = l, r
                
                temp = matrix[t][l + i]                    # save top left in temp
    
                matrix[t][l + i] = matrix[b-i][l]          # top left = bottom left
                matrix[b-i][l] = matrix[b][r-i]            # bottom left = bottom right
                matrix[b][r-i] = matrix[t+i][r]            # bottom right = top right
                matrix[t+i][r] = temp                      # top right = top left
                
            r -= 1
            l += 1
                
        
            