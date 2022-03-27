class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        alphabet = {}
        
        for i in s:
            if alphabet.get(i):
                alphabet[i] += 1
            else:
                alphabet[i] = 1
                
        for i in t:
            if alphabet.get(i):
                alphabet[i] -= 1
            else:
                return False
            
        for i in alphabet:
            if alphabet[i] > 0:
                return False
            
        return True