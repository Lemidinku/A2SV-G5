# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        for i in range(32):
            if (xor>>i)&1:
                zeros = 0
                ones = 0
                for num in nums:
                    if (num>>i)&1:
                        ones ^= num
                    else:
                        zeros ^= num
                return [zeros, ones]