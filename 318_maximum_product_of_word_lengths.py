class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_rep = [None] * len(words)
        
        for w in range(len(words)):
            res = 0
            for l in words[w]:
                res |= 1 << (ord(l) - 97)
            bit_rep[w] = res
        
        max_len = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                if bit_rep[i] & bit_rep[j] == 0: max_len = max(max_len, len(words[i]) * len(words[j]))
            
        return max_len
