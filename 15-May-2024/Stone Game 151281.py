# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def minimize(left, right):
            if left>right:
                return 0
            takeLeft = maximize(left+1,right) + piles[left]
            takeRight = maximize(left,right-1) +piles[right]
            return min(takeLeft ,takeRight)
        @cache
        def maximize(left, right):
            if left>right:
                return 0
            takeLeft = minimize(left+1,right) + piles[left]
            takeRight = minimize(left,right-1) +piles[right]
            return max(takeLeft ,takeRight)
        result = maximize(0,len(piles)-1)
        return result >0