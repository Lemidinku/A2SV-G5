class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        cons = 0
        curr = 0
        for num in nums:
            if num ==1:
                curr +=1
                cons = max(curr, cons)
            else:
                curr = 0
        return cons        