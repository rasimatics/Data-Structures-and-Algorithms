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


    # second way to find also indices
    prices = [1,4,2]
    def max_profit(self, prices):
        buy_price = prices[0]
        buy_day = 1
        bought_day = 1
        sold_day = 1
        profit = 0

        day = 1
        for price in prices:
            if price < buy_price:
                buy_price = price
                buy_day = day

            if profit < price - buy_price:
                profit = price - buy_price
                bought_day = buy_day
                sold_day = day

            day += 1
        
        print(f"{profit=} {bought_day=} {sold_day=}")

        return profit




        