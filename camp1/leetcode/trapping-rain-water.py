class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        ans = 0

        for i in range(len(height)):
            inbetween_height = 0
            while stack and height[stack[-1]] <= height[i]:
                ans += (min(height[stack[-1]], height[i])-inbetween_height) *(i-stack[-1]-1)

                inbetween_height = height[stack.pop()]
            
            

            if stack and i-stack[-1]>0:
                ans += (min(height[stack[-1]], height[i])-inbetween_height) *(i-stack[-1]-1)
            stack.append(i)
            
        
        return ans
