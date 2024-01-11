class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        freq = defaultdict(int)
        max_sum = 0
        summ = 0

        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            summ += nums[right]

            while freq[nums[right]] > 1:
                freq[nums[left]]-=1
                summ -= nums[left]
                left+=1
            max_sum = max(max_sum, summ)
            

        return max_sum 
        