class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        minn = 0
        summ = 0
        max_sum = float('-inf')
        for num in nums:
            summ += num
            max_sum = max(max_sum, summ-minn)
            minn = min(minn, summ)

        return max_sum