class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.cache = {}
        ans = 0
        for move in range(1, maxMove + 1):
            ans += self.backtrack(m, n, startRow, startColumn, move)
        return ans % (pow(10, 9) + 7)
    
    def backtrack(self, m, n, r, c, move):
        if (r,c,move) in self.cache:
            return self.cache[(r,c,move)]
        
        if move == 1:
            val = 0
            
            if r - 1 < 0 : val += 1
            if r + 1 >= m: val += 1
            if c + 1 >= n: val += 1
            if c - 1 < 0: val += 1
            
            self.cache[(r,c,move)] = val
            
            return val
            
        else:
            res = 0

            if r - 1 >= 0:
                res += self.backtrack(m, n, r - 1, c, move - 1)
            if r + 1 < m: 
                res +=  self.backtrack(m, n, r + 1, c, move - 1)
            if c - 1 >= 0: 
                res += self.backtrack(m, n, r, c - 1, move - 1)
            if c + 1 < n: 
                res += self.backtrack(m, n, r, c + 1, move - 1)
            
            self.cache[(r,c,move)] = res
            return res
