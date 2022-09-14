class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        dp = [0] * len(nextVisit)
        MOD = 10 ** 9 + 7
        day = 0
        
        for i in range(0, len(nextVisit)-1):
            day += day - dp[nextVisit[i]] + 2
            day = day % MOD
            dp[i+1] = day
        
        return dp[-1]
    
    
    def firstDayBeenInAllRooms2(self, nextVisit: List[int]) -> int:
        dp = [0] * len(nextVisit)
        MOD = 10 ** 9 + 7
        
        for i in range(0, len(nextVisit)-1):
            dp[i + 1] = ( dp[i] - dp[nextVisit[i]] + dp[i] + 2 ) % MOD
        
        return dp[-1]
            
            
        
    # Time Limit Exceeded
    def firstDayBeenInAllRooms3(self, nextVisit: List[int]) -> int:
        day = 0
        visit_times = {}
        
        i = 0
        while i != len(nextVisit) - 1:
            visit_times[i] = visit_times.get(i, 0) + 1
            
            if visit_times[i] % 2 == 0:
                i = (i + 1) % len(nextVisit)
            else:
                i = nextVisit[i]
            
            day += 1
        
        return day
