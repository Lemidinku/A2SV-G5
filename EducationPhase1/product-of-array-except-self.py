class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1]
        post_prod = [1]

        for i in range(len(nums)-1):
            pre_prod.append(pre_prod[-1]*nums[i])
        
        for i in range(len(nums)-1,0,-1):
            post_prod.append(post_prod[-1]*nums[i])

        output = []
        for i in range(len(pre_prod)):
            output.append(pre_prod[i]*post_prod[len(pre_prod)-1-i])
        return output

