class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            k = i
            num = nums[i]
            while k > 0 and num < nums[k-1]:
                nums[k] = nums[k-1]
                k -= 1
            nums[k] = num
