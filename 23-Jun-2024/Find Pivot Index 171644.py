# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_sum = [0]
        post_sum = [0]
   
   
        for i in range(1,len(nums)):
            pref_sum.append(pref_sum[-1]+nums[i-1])

        for i in range(len(nums)-2,-1,-1):
            post_sum.append(post_sum[-1]+nums[i+1])
        
        i=0
        while i<len(pref_sum):
            if pref_sum[i]==post_sum[len(post_sum)-i-1]: return i
            i+=1
        return -1


        # [0,1,8,11,17,22]
        # [0,6, 11, 17, 20, 27]