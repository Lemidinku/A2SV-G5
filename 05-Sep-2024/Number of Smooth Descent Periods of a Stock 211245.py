# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        prev  = 0
        ans = 0
        for i in range(n):
            if prices[i]+1 != prices[i-1]:
                prev = i
            ans += i-prev+1
        
        return ans
