class Solution:
    def isHappy(self, n: int) -> bool:
        t = 0
        while t < 9:
            m = 0
            for a in str(n):
                m += int(a)**2
            n = m
            if n == 1:
                return True
            t += 1