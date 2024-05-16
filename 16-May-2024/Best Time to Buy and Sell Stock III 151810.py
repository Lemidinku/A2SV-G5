# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minn_cost = float('inf')
        ans = [0]*n
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, prices[i]-minn_cost)
            ans[i] = max_profit
            minn_cost = min(prices[i], minn_cost)
        
        max_cost = float('-inf')
        arr = [0]*n
        max_profit = 0
        for i in reversed(range(n)):
            max_profit = max(max_profit, max_cost-prices[i])
            ans[i] += max_profit
            max_cost = max(prices[i], max_cost)

        return max(ans)