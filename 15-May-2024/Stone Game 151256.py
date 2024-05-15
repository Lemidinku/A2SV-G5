# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def recur(left,right,turn):

            if left>right:
                return 0
            
            if not turn:
                takeLeft = recur(left+1,right,1-turn) + piles[left]
                takeRight = recur(left,right-1,1-turn) +piles[right]
                return max(takeLeft ,takeRight)
            else:
                takeLeft = recur(left+1,right,1-turn)-piles[left]
                takeRight = recur(left,right-1,1-turn)-piles[right]
                return min(takeLeft,takeRight)

        result = recur(0,len(piles)-1,0)
        return result >0