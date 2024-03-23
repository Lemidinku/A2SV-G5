class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def lessThanThreshold(divisor):
            summ = 0
            for num in nums:
                summ += math.ceil(num/divisor)
            return summ<= threshold


        left = 1
        right = max(nums)

        while left<=right:
            mid = left + (right-left)//2

            if lessThanThreshold(mid):
                right = mid-1
            else:
                left = mid+1

        return left