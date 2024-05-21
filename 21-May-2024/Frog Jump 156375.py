# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        n = len(stones)
        @cache
        def backtrack(i,last_jump):
            if i==n-1:
                return True
            ans = False
            for j in range(i+1,n):
                next_jump = stones[j]-stones[i]
                if next_jump == last_jump-1 or next_jump==last_jump or next_jump==last_jump+1:
                    ans |=backtrack(j,stones[j]-stones[i])

                    
            return ans
        
        return backtrack(0,0)