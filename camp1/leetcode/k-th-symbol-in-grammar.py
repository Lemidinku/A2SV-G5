class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def find_bit(height,ind):
            if height==0:
                return 0
            val = find_bit(height-1, ind//2)
            return (val+ ind%2)%2
           
        
        return find_bit(n-1,k-1)