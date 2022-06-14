class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for word in words:
            if word == s[:len(word)]:
                res += 1
        return res
    
    def countPrefixes2(self, words: List[str], s: str) -> int:
        res = 0
        for word in words:
            if word in s and word[0] == s[0] and word[-1] == s[len(word)-1]:
                res += 1
        return res