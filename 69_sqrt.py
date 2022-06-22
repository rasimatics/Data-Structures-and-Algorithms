class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        
        start = 0
        end = x
                
        while start <= end:
            mid = (start + end) // 2
            if x >= mid * mid and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid + 1