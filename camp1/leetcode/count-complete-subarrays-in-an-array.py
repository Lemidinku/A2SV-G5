class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count =0
        left = 0
        uniques  = len(set(nums))


        window = {}
        for right in range(n):
            if nums[right] in window:
                window[nums[right]] +=1
            else:
                window[nums[right]] =1
            
            while len(window) == uniques:
                count += n - right
                window[nums[left]] -=1
                if not window[nums[left]]: del window[nums[left]]

                left +=1
        return count