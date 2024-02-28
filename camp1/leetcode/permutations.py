class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr_permute = []
        def backtrack():
            if len(curr_permute)==len(nums):
                permutations.append(curr_permute[:])
                return
            for num in nums:
                if num not in curr_permute:
                    curr_permute.append(num)
                    backtrack()
                    curr_permute.pop()

            
        backtrack()

        return permutations

