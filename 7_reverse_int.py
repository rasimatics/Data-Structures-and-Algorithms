class Solution:
    def reverse(self, x: int) -> int:
        if x < -2147483648  or x > 2147483648:
            return 0
        
        is_negative = True if x < 0 else False
        x = abs(x)
        
        rev = 0
        while x > 0:
            rev = rev*10 + x%10
            x //= 10
            
        rev = int(rev)
        
        if rev > 2147483648:
            return 0
        
        return -rev if is_negative else rev
        