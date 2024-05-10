# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn_cost = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price-minn_cost)
            minn_cost = min(price, minn_cost)
        return max_profit