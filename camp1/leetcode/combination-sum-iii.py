class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = []
        self.summ = 0
        combs = []
        def backtrack(i):
            if self.summ==n:
                if nums not in combs and len(nums)==k:
                    combs.append(nums[:])
                return
            if i>9 or self.summ>n:
                return 

            backtrack(i+1)
            self.summ += i
            nums.append(i)

            backtrack(i+1)
            self.summ -= i
            nums.pop()
        backtrack(1)
        return combs
        