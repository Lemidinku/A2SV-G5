# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for num in range(amount+1):
            ans = dp[num]
            for j in range(len(coins)):
                if num -coins[j]>=0:
                    ans = min(ans, dp[num -coins[j]]+1)
            dp[num] = ans
        min_coins = dp[amount]
        return min_coins if min_coins<float('inf') else -1
                    

