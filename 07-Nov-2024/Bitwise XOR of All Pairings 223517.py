# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n , m = len(nums1), len(nums2)

        xor = 0
        if m%2: 
            for num in nums1: xor ^= num
        if n%2: 
            for num in nums2: xor ^= num

        return xor

