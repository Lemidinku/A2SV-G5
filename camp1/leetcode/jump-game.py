class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for a in range(len(nums)-1):
            curr-=1
            curr = max(curr,nums[a])
            if curr==0: 
                return False
        return True


        