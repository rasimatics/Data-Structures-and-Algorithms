from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        profit = 0
        
        while p2 < len(prices):
            if prices[p2] - prices[p1] > profit:
                profit = prices[p2] - prices[p1]
            elif prices[p2] - prices[p1] <  0:
                p1 = p2
            p2 += 1
        
        return profit if profit > 0 else 0
        