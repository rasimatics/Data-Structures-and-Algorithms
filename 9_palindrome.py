class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        tmp = abs(x)
        rev = 0
        while tmp > 0:
            rev = rev * 10 + tmp % 10
            tmp = tmp // 10
        
        if abs(x) == rev :
            return True
        return False
        
    
    def isPalindrome2(self, x: int) -> bool:
        reverse = str(abs(x))[::-1]
        return x == int(reverse)
        