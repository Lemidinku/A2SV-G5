# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        i=0
        num = 1
        
        while num <= n:
            if n%num ==0:
                i+=1
            if i==k:
                return num
            num+=1

        return -1
