# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float('inf')]*(1<<n)
        dp[0] = 0
        for mask in range(1<<n):
            indx = bin(mask).count('1')
            for i in range(n):
                if not (mask & (1<<i)):
                    new_mask = mask | (1<<i)
                    dp[new_mask] = min(dp[new_mask], dp[mask]+(nums1[indx]^nums2[i]))

        return dp[-1]
                    