# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)/k
        n = len(nums)
        @cache
        def backtrack(mask,summ):
            if mask==(1<<(n))-1:
                if summ==target:
                    return True
                return False
            
            if summ==target:
                summ=0

            ans=False
            for i in range(n):
                if not mask &(1<<i) and summ+nums[i]<=target:
                    ans |=backtrack(mask|(1<<i), summ+nums[i])
            return ans
        
        return backtrack(0,0)


