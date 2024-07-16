# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        
        max_diff = 0
        for i in range(len(nums)-1):
            max_diff = max(max_diff, nums[i+1]-nums[i])
        return max_diff