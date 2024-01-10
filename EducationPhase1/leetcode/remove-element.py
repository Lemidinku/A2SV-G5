class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return nums.sort()
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i] = "a"
        nums.sort()
        while nums[-1] == "a":
            
            nums.pop()
            if len(nums) == 0:
                break
        return nums.sort()