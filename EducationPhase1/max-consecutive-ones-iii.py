class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        max_len =0
        left = 0
        for right in range(len(nums)):
            if not nums[right]: zeros+=1
        
            while zeros > k:
                if not nums[left]: zeros-=1
                left+=1
            
            max_len = max(max_len, right-left+1)
        return max_len