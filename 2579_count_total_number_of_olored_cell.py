class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        elif n >= 3:
            return self.coloredCells(n-1) + 4 + (n - 2) * 4
        else:
            return self.coloredCells(n - 1) + 4

        

        
