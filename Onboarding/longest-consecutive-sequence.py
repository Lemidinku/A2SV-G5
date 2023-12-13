class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        longest = 1
        for num in nums:
            if num-1 not in nums_set:
                leng = 0
                while num in nums_set:
                    leng +=1
                    num += 1
                longest = max(longest,leng)
        return longest

                
