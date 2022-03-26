class Solution:    
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        
        for i in range(0, n):
            tmp = second
            second = first + second
            first = tmp
        return second
    
    # second recursive way     
    def climbStairs2(self, n: int) -> int:
        if n<2:
            return 1
        left = self.climbStairs(n-1)
        right = self.climbStairs(n-2)
        return left + right
    
    # not count print number of ways - all combinations
    def climbStairs3(self):
        pass

test = Solution() 
print(test.climbStairs(4)) # 5