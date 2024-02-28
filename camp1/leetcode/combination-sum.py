class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = []
        self.summ = 0
        combs = []
        def backtrack(i):
            if self.summ==target:
                if nums not in combs:
                    combs.append(nums[:])
                return
            if i>=len(candidates) or self.summ>target:
                return 
            # use the same number again
            nums.append(candidates[i])
            self.summ += candidates[i]
            backtrack(i)
            nums.pop()
            self.summ -= candidates[i]


            self.summ += candidates[i]
            nums.append(candidates[i])
            backtrack(i+1)
            nums.pop()
            self.summ -= candidates[i]
            
            backtrack(i+1)
        backtrack(0)
        return combs
        




