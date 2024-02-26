class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.combs = []
        def backtrack(arr,i):
            if len(arr)==k:
                self.combs.append(arr[:])
                return
            if i>n: 
                return

            arr.append(i)
            backtrack(arr,i+1)
            arr.pop()
            backtrack(arr,i+1)


        backtrack([],1)
        return self.combs