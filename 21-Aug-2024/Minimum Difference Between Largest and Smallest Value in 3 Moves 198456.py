# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
            if len(nums)<5: return 0
            nums.sort()
            
            min_diff = min(nums[-1]-nums[3],
                        nums[-2]-nums[2],
                        nums[-3]-nums[1],
                        nums[-4]-nums[0]
                        )
            
            
            return min_diff