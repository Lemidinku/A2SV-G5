# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        @cache
        def backtrack(i,summ):
            if i >= len(nums):
                return summ == target
            if summ > target:
                return False
            return backtrack(i+1, summ+nums[i]) or backtrack(i+1, summ)
        
        return backtrack(0,0)