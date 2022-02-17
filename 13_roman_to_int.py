class Solution:
    def romanToInt(self, s: str) -> int:
        alp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)-1):
            if alp[s[i]] >= alp[s[i+1]]:
                ans += alp[s[i]]
            else:
                ans -= alp[s[i]]
        ans = ans + alp[s[-1]]
        return ans
            

test = Solution() 
print(test.romanToInt("MCMXCIV")) #1994