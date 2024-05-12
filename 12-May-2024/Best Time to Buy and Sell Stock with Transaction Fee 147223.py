# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = {}
        def buy_sell(i, buy):
            if (i,buy) in dp:
                return dp[(i,buy)] 
            if i>=n:
                return 0
            if buy:
                a = buy_sell(i+1, not buy)-prices[i]
                b = buy_sell(i+1, buy)
                dp[(i,buy)] = max(a,b)
            else:
                a = buy_sell(i+1, not buy)+prices[i]-fee
                b = buy_sell(i+1, buy)
                dp[(i,buy)] = max(a,b) 
            return dp[(i,buy)]
        
        return buy_sell(0,True)