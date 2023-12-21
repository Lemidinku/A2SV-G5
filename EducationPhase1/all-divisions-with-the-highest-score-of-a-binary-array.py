class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        tot_sum = sum(nums) # O(n)
        ones = 0
        max_score = float("-inf")
        max_arr  = []

        for i in range(len(nums)+1):
        
            score = i + tot_sum - 2*ones
            if score > max_score:
                max_score = score
                max_arr = [i]
            elif score == max_score:
                max_arr.append(i)

            if i<len(nums)  and nums[i]: ones+=1

        return max_arr