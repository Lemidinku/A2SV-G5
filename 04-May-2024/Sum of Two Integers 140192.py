# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        i = 0
        ans = 0
        carry = 0
        for i in range(32):
            num1, num2= a&(1<<i), b&(1<<i)
            if num1:
                carry +=1
            if num2:
                carry +=1
            ans |= (carry%2 << i)
            carry//=2
        if ans >= (1 << 31):
            ans -= (1 << 32)
        return ans

        #010
        #011