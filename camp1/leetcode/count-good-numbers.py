class Solution:
    def countGoodNumbers(self, n: int) -> int:
        result = pow(20, n//2,(10**9 + 7))
        if n%2:
            result *= 5 

        return (result)%(10**9 + 7)

        # def count(n):
        #     if not n: return 1
        #     return (20*count(n-2))% (10**9 +7)
        
        # result = 1
        # if n%2:
        #     result = count(n-1)*5
        # else: 
        #     result = count(n)
        
        # return (result)%(10**9 + 7)