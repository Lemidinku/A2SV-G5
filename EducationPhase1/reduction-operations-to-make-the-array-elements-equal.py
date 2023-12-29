class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        # nums.sort()
        maxx  = max(nums)+1
        count = [0]*maxx
        for num in nums:
            count[num] +=1
        
        nums = []
        for i in range(maxx):
            if count[i]:
                nums += [i]*count[i]
        
        prev = nums[0]
        ops = 0
        tot_ops = 0

        for num in nums:
            if num != prev:
                ops += 1
                prev  = num
            tot_ops += ops

        return tot_ops
