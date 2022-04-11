class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverse(matrix)
        
        
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

                
    def reverse(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                tmp = matrix[i][j] 
                matrix[i][j]  = matrix[i][len(matrix) - j -1] 
                matrix[i][len(matrix) - j -1] = tmp

    
    def rotate2(self, matrix: List[List[int]]) -> None:
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
                
        
            