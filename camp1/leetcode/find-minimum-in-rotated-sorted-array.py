class Solution:
    def findMin(self, nums: List[int]) -> int:
        left =0
        right =len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]< nums[0]:
                right = mid-1
            else:
                left = mid+1
        return nums[left] if left<len(nums) else nums[0]