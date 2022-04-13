class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        
        common = self.find_prefix_between_two(strs[0], strs[1])
        for i in range(2, len(strs)):
            common = self.find_prefix_between_two(common, strs[i])
            
            if common == "":
                break
        
        return common
        
        
    def find_prefix_between_two(self, word1, word2):
        length = len(word1) if len(word1) < len(word2) else len(word2)
        i = 0
        while i < length:
            if not word1[i] == word2[i]:
                return word1[:i]
            
            i += 1
        
        return word1[:i]
            
                
                
            
            