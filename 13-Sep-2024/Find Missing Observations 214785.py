# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        val= sum(rolls)
        summ = ((m+n)*mean)-val
        if summ < n: return []
        a = summ//n
        if a > 6: return []
        rem = summ%n
        ans = [a]*(n-rem) + [a+1]*rem
        if ans[-1] > 6: return []

        return ans