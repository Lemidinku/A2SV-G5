# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def __init__(self):
        self.cache = {}
    def tribonacci(self, n: int) -> int:
        if not n: return 0
        elif n<3:
            return 1
        elif n in self.cache:
            return self.cache[n]
        
        ans = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.cache[n]=ans
        return ans
        