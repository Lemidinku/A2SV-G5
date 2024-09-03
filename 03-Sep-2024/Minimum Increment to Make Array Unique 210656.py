# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        count = 0
        curr = nums[0]+1

        for num in nums[1:]:
            if num < curr:
                count += curr-num
            elif num > curr:
                curr = num
            curr +=1
        return count