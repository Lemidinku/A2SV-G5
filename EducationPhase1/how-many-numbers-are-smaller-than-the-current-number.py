from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(bisect_left(sorted_nums,num))

        return result

            