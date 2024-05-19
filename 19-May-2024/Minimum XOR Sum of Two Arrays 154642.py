# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @cache
        def dp(i, mask):
            print(i,bin(mask))
            if i==n:
                return 0
            
            ans = float('inf')
            for j in range(n):
                if not (mask&(1<<j)):
                    ans = min(ans, (nums1[i]^nums2[j]) + dp(i+1, mask|(1<<j)))
            return ans
        return dp(0,0)

                    