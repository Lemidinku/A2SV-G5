# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        dp = {}
        for i in range(n+1):
            count = 0
            while i > 0:
                if i in dp:
                    count += dp[i]
                    break
                if i&1 == 1:
                    count += 1
                i >>= 1
            dp[i] = count
            ans.append(count)
        return ans