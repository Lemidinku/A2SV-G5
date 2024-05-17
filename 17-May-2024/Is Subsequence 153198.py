# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        row = len(s)
        col = len(t)

        dp = [[False]*(col+1) for _ in range(row+1)]

        for i in range(col+1):
            dp[0][i] = True

        for r in range(1,row+1):
            for c in range(1,col+1):
                dp[r][c] = dp[r][c-1]
                if s[r-1]==t[c-1]:
                    dp[r][c] = True
                dp[r][c] &= dp[r-1][c-1]
        return dp[row][col]

                
            
        


            
