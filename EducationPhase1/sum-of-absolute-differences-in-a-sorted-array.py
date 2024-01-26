class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n =len(nums)
        pref_diff = [0]*n
        tot_diff = 0

        for i in range(1,n):
            tot_diff += abs(nums[i]-nums[i-1])* (i)
            pref_diff[i] = tot_diff

        suff_diff = [0]*n
        tot_diff = 0

        for i in range(n-2,-1,-1):
            tot_diff += abs(nums[i]-nums[i+1]) * (n-i-1)
            suff_diff[i] = tot_diff

        result=[0]*n
        for i in range(n):
            result[i] = pref_diff[i] + suff_diff[i]


        return result
