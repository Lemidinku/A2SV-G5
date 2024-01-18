class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float('inf')
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                summ = nums[i] + nums[left] + nums[right]
                if abs(summ-target) < abs(closest-target):
                    closest = summ

                
                if summ > target:
                    right -=1
                else:
                    left += 1

               
        return closest