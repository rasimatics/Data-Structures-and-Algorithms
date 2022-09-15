class Solution:
    def checkRecord(self, s: str) -> bool:
        absent= 0
        
        for j in range(len(s)):
            i = s[j]
            
            if i == "A":
                absent += 1
            
            if absent > 1:
                return False
            
            if i == "L" and j > 0 and s[j-1] == "L" and j < len(s) - 1 and s[j+1] == "L":
                return False
            
        return True
        
