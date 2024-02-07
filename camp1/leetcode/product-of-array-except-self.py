class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        pro =1
        for i in range(len(nums)):
            pre[i]=pro
            pro *= nums[i]


        suf = [1]*len(nums)
        pro =1
        for i in range(len(nums)-1, -1, -1):
            suf[i]=pro
            pro *= nums[i]

        
        for i in range(len(nums)):
            suf[i]*=pre[i]
        return suf


        
