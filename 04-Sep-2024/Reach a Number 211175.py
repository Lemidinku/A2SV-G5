# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        moves = 0
        summ  = 0

        while summ < target or (summ-target)%2:
            summ +=(moves+1)
            moves +=1
        
        return moves
