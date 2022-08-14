class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        
        for i in strs:
            key = self.get_key(i)
            final_dict[key] = final_dict.get(key, []) + [i,]
            
        return final_dict.values()
            
            
        
        
    def get_key(self, word):
        alph = [0] * 26
        
        for i in word:
            alph[ord(i) - ord("a")] += 1
        
        return str(alph)
        