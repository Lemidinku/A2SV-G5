# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        @cache
        def backtrack(i,k):
            if i==target:
                return True
            ans= False
            if i+k+1 in stones:
                ans |=backtrack(i+k+1, k+1)
            if k>0 and  i+k in stones:
                ans |=backtrack(i+k, k)
            if k>0 and  i+k-1 in stones:
                ans |=backtrack(i+k-1, k-1)
            return ans
        
        return backtrack(0,0)