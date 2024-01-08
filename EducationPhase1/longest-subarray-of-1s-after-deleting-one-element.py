class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones = 0
        zeros = 0
        max_len =0
        left = 0
        for right in range(len(nums)):
            if not nums[right]: zeros+=1
        
            while zeros > 1:
                if not nums[left]: zeros-=1
                left+=1
            
            max_len = max(max_len, right-left)
        return max_len
