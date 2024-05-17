# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n,m = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i>0:
                        dp[i][j] += dp[i-1][j]
                    if j>0:
                        dp[i][j] += dp[i][j-1] 

        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0 
        return dp[m-1][n-1]
                    