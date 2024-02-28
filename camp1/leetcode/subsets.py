class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        
        def backtrack(i, combination): 
            if i >= len(nums):
                combinations.append(combination[:])
                return
            
            combination.append(nums[i])
            backtrack(i+1, combination)
            combination.pop()
            
            backtrack(i+1, combination)
            
        backtrack(0, [])
        return combinations