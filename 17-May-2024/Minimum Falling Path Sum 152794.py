# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        dp = [[0]*n for _ in range(n)]
        for row in range(n-1, -1, -1):
            for col in range(n):
                if row==n-1:
                    dp[n-1][col] = matrix[n-1][col]
            
                else:
                    prev_sum = dp[row+1][col]
                    if col > 0:
                         prev_sum = min( prev_sum,dp[row+1][col-1])
                    if col < n-1:
                         prev_sum = min( prev_sum,dp[row+1][col+1])
                    dp[row][col] = prev_sum+matrix[row][col]

        min_sum = float('inf')
        for i in range(n):
            min_sum = min(min_sum, dp[0][i])                   

        return min_sum



