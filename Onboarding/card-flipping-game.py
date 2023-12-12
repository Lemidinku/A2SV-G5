class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        possible = set(fronts+backs)
        for num1,num2 in zip(fronts,backs):
            if num1==num2:
                possible.discard(num1)
        return min(possible) if possible else 0
        

