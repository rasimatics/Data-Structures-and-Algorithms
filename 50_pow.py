class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        cur_product = x
        i = abs(n)
        
        while i > 0:
            if i % 2 == 1:
                res *= cur_product
            
            cur_product *= cur_product
            i = i // 2
        
        return res if n > 0 else 1 / res