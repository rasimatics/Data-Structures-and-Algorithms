class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        is_negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        while divisor <= dividend:
            tmp, i = divisor, 1
            
            while tmp <= dividend:
                dividend -= tmp
                res += i
                tmp += tmp
                i += i
        
        if is_negative:
            res = -res
        
        return max(-2147483648, min(2147483647,res))