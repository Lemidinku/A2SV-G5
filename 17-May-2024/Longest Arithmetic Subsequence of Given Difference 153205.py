# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        
        dp = defaultdict(int)
        maxx = 0
        for num in arr:
            dp[num] = dp[num-difference] + 1
            maxx = max(maxx, dp[num])
        return maxx
        
        
       