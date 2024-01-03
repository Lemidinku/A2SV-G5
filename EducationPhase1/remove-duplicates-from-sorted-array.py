class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2: return nums[0]
        left = 0
        for right in range(1,len(nums)):
            if nums[right]==nums[left]:
                nums[right] = "_"
                
            else:
                left = right

        holder  = 0
        for seeker in range(len(nums)):
            if nums[seeker] != "_":
                nums[holder],nums[seeker]  = nums[seeker], nums[holder]
                holder +=1
        return holder
            

        
