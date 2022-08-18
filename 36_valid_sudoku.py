class Solution:
    # O(n^2) solution
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        _dict = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                midX = (i // 3) * 3 + 1
                midY = (j // 3) * 3 + 1
                
                if f"{num}-{i}-x" in _dict or f"{j}-{num}-y" in _dict or f"{midX}-{midY}-{num}-m" in _dict:
                    return False
                
                if num != ".":
                    _dict[f"{num}-{i}-x"] = 1
                    _dict[f"{j}-{num}-y"] = 2               
                    _dict[f"{midX}-{midY}-{num}-m"] = 3     
                    
        return True
    
    # first solution O(n^3)
    def isValidSudoku2(self, board: List[List[str]]) -> bool:        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                #check left to right
                if board[i][j] != '.' and board[i].count(board[i][j]) > 1:
                    return False
            
                # check top to bottom
                for k in range(len(board)):
                    if i != k and board[i][j] != "." and board[k][j] == board[i][j]:
                        return False
                
            
                # check inner 9 nums
                startX = (i // 3) * 3
                endX = startX + 3
                
                startY = (j // 3) * 3
                endY = startY + 3
                
                for x in range(startX, endX):
                    for y in range(startY, endY):
                        if x != i and y != j and board[i][j] != "." and board[i][j] == board[x]:
                            return False
        return True
                
        
