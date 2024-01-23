class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        pref = 0

        for i in range(len(nums)):
            tot_sum -= nums[i]
            if pref==tot_sum:
                return i
            pref += nums[i]
        return -1