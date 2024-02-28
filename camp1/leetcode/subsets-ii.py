class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        curr_set= []
        def backtrack(i):
            if i>=len(nums):
            
                if sorted(curr_set) not in subsets:
                    subsets.append(sorted(curr_set))
                return

            backtrack(i+1)
            curr_set.append(nums[i])

            backtrack(i+1)
            curr_set.pop()

        backtrack(0)

        return subsets
            