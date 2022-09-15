class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        len_part = len(part)
        len_s = len(s)
        i = 0
        
        while i < len_s:      
            if s[i:i+len_part] == part:
                s = s[:i] + s[i+len_part:]
                len_s = len(s)
                i = 0
            else:
                i += 1
        
        return s
