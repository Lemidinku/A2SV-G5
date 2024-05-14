# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort(reverse=True)
        @cache
        def dp(needed_amount, i):
            if needed_amount == 0:
                return 1
            
            ways = 0
            for j in range(i, n):
                if coins[j] <= needed_amount:
                    ways += dp(needed_amount-coins[j], j)
            return ways
        return dp(amount, 0)
                
                

            