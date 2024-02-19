class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        def canMinimizetoK(arr,k):
            left_over = 0

            for num in arr[::-1]:
                if num >= k:
                    left_over += num-k
                else:

                    left_over -= k-num
                    if left_over < 0: left_over = 0
            if left_over:
                return False
            return True



        left = min(nums)
        right = max(nums)
        
        while left<=right:
            mid =( right + left)//2
            if canMinimizetoK(nums,mid):
                right = mid -1
            else:
                left = mid + 1

        return left

                
