# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg = [x for x in nums if x<0]
        pos = [x for x in nums if x>0]
        result = []
        for i in range(len(nums)//2):
            result.append(pos[i])
            result.append(neg[i])
        return result

    