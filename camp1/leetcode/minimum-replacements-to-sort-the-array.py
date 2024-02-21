class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        count = 0
        curr = nums[-1]
        for i in reversed(range(len(nums)-1)):
            print(i,nums[i], curr)
            if nums[i] > curr:
                spots = math.ceil(nums[i]/curr)  
                curr = nums[i]//spots
                count += spots-1
            else:
                curr = nums[i]
        return count


