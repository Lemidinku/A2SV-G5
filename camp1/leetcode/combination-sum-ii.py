class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidates.insert(0,-1)
        nums = []
        self.summ = 0
        combs = []
        def backtrack(i):
            if self.summ==target:
                combs.append(nums[:])
                return
            if  i>= len(candidates) or self.summ>target:
                return 
            
            lastone = -1
            for j in range(i+1,len(candidates)):
                if  candidates[j] != lastone:
                    self.summ += candidates[j]
                    nums.append(candidates[j])
                    backtrack(j)
                    self.summ -= candidates[j]
                    nums.pop()
                    lastone = candidates[j]


            
        backtrack(0)
        return combs