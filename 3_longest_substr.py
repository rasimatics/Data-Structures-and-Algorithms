class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 0
        length = 0
        sub = {}
        
        while p2 < len(s):
            if s[p2] not in sub:
                sub[s[p2]] = sub.get(s[p2], 0) + 1
                p2 += 1
                length = max(length, len(sub))
            else:
                sub.pop(s[p1])
                p1 += 1
        return length
                
    
    """
        My First Solution
    """
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) == 0: return 0
        
        p1, p2 = 0, 0
        length = 0
        sub = {}
        
        while p1 < len(s) and p2 < len(s):
            sub[s[p2]] = sub.get(s[p2], 0) + 1
            
            if sub[s[p2]] > 1:
                length = max(length, p2 - p1)
                p1 += 1
                p2 = p1
                sub = {}
            else:
                p2 += 1
        
        length = max(length, p2 - p1)
        return length
                
                

            