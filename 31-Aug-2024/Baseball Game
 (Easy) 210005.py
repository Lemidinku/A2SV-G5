# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lis = []
        for op in operations:
            if op == "+": lis.append(lis[-1]+lis[-2])
            elif op == "D": lis.append(lis[-1]*2)
            elif op == "C": lis.pop()
            else: lis.append(int(op))
        return sum(lis)
