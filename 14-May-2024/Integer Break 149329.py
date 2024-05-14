# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def dp(num):
            if num == 2:
                return 2
            if num == 3:
                return 3

            maxx = 0
            for i in range(2, num):
                maxx = max(maxx, dp(num-i)*i)
            return maxx
        if n==2: return 1
        if n==3: return 2
        return dp(n)
