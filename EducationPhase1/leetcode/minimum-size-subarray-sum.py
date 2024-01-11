class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        min_len = float("inf")
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ>=target:
                min_len = min(min_len, right-left+1)
                summ-=nums[left]
                left +=1

        if min_len<=len(nums):
            return min_len
        return 0


