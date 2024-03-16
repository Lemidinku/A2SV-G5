class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canMake(maxx):
            if maxx<max(nums): return False
            segments = 1
            summ =0
            for num in nums:
                if summ+num>maxx:
                    summ =0
                    segments +=1
                summ+=num
            return segments <= k
            
        left = 0
        right = sum(nums)


        while left<=right:
            mid = left + (right-left)//2
            if canMake(mid):
                right = mid-1
            else:
                left = mid+1
        
        return left