# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lis = [(pos,sp) for pos,sp in zip(position,speed) ]
        lis.sort(reverse=True)

        stack = [] #increasing monotonic stack
        for x,v in lis:
            t = (target-x)/v
            if not stack or (stack and stack[-1]<t):
                stack.append(t)

        return len(stack)
