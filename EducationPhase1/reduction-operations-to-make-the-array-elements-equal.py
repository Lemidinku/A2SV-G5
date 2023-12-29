class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        prev = nums[0]
        ops = 0
        tot_ops = 0

        for num in nums:
            if num != prev:
                ops += 1
                prev  = num
            tot_ops += ops

        return tot_ops
