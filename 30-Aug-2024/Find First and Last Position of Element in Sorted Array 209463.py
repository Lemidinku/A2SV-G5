# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from bisect import bisect_left , bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect_left(nums,target)
        y =bisect_right(nums,target)
        left = x if x<len(nums) and nums[x]==target else -1
        right = y-1 if y>0 and nums[y-1]==target else -1

        return [left, right]
