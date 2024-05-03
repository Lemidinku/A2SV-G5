# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        val = 2**maximumBit-1
        xor = 0
        for num in nums:
            xor ^=num
        xor ^=val
        ans = []
        for num in nums[::-1]:
            ans.append(xor)
            xor ^=num
        return ans
