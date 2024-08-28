# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:  
    def nthUglyNumber(self, n: int) -> int:
        # if n==1: return 1
        uglies = [1]
        p2,p3, p5 = 0, 0, 0
        num = 1
        i=1
        while i<n:
            num = min(uglies[p2]*2, uglies[p3]*3, uglies[p5]*5)
            uglies.append(num)
            if num==uglies[p2]*2:
                p2+=1
            if num==uglies[p3]*3:
                p3+=1
            if num==uglies[p5]*5:
                p5+=1
            i+=1
        return num

            
