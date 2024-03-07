class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        n = len(heights)

        stack = []
        maxx = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1]>heights[i]:
                s,val = stack.pop()
                area = (i-s) *(val)
                maxx = max(maxx, area)
                start = s
            stack.append((start,heights[i]))
        
        return maxx

        