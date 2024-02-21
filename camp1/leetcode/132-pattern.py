class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        mins = [float(inf)]*len(nums)

        for i in range(len(nums)):
            if stack:
               mins[i] = min(nums[stack[-1]], mins[stack[-1]])
            while stack and nums[stack[-1]]< nums[i]:
               stack.pop()
            
            if stack and mins[stack[-1]]<nums[i]<nums[stack[-1]]:
                return True
            stack.append(i)
        return False

# [3,5,0,3,4]
            

