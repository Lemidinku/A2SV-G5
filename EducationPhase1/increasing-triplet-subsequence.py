class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        left_min = [0]*n
        minn = float("inf")
        for i in range(n):
            left_min[i] = minn
            minn = min(minn,nums[i])
        
        right_max = [0]*n
        maxx = float("-inf")
        for i in range(n-1,-1,-1):
            right_max[i] = maxx
            maxx = max(maxx,nums[i])

        for i in range(n):
            if left_min[i]<nums[i]<right_max[i]:
                return True
        return False