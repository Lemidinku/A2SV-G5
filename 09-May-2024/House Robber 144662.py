# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len(nums)
        memo = [-1 for _ in range(n)]
        def dp(i):
            if i>=n:
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i] = max(dp(i+1), nums[i]+dp(i+2))
            return memo[i]
        return dp(0)
        
        # n = len(nums)
        # dp = [0]*n
        
        # max_money =0
        # for i in range(n):
        #     prev_money = 0
        #     for j in range(i-1):
        #         prev_money = max(prev_money, dp[j])
        #     dp[i] = prev_money + nums[i]
        #     max_money = max(max_money, dp[i])
        # return max_money
