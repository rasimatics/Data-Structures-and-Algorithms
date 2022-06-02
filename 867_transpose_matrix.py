class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:        
        col = len(matrix)
        row = len(matrix[0])
        
        ans = [[None]*col for _ in range(row)]
        
        for i in range(col):
            for j in range(row):
                ans[j][i] = matrix[i][j]
                
        return ans