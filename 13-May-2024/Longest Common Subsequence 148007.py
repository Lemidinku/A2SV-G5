# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text2), len(text1)

        dp = [[0]*n for _ in range(m)] 
        max_len =0

        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    prev = dp[i-1][j-1] if i and j else 0
                    dp[i][j] = prev + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

                max_len = max(max_len, dp[i][j])
        


        return max_len

