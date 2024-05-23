# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_nums = []
        i = 1
        while i * i <= n:
            perfect_nums.append(i * i)
            i += 1


        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            for perfect in perfect_nums:
                if i-perfect>=0:
                    dp[i] = min(dp[i], 1+dp[i-perfect])
        return dp[-1]
        # return 0        
