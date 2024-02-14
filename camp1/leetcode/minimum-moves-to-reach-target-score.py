class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        


        num = target
        ops =0
        while num>1:

            if maxDoubles:
                if num%2: ops +=1
                num //= 2
                ops +=1
                maxDoubles-=1

            else:
                ops+=num-1
                num=1

        return ops


