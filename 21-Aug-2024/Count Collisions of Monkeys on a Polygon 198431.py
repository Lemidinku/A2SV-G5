# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10**9+7
        ans = pow(2,n,mod)-2

        # for testcase 82/83 : n=500000003
        if ans<0: ans+=mod
        
        return ans