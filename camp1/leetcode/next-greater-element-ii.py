class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 1,2,3,4,3,1,2,3,4,3
        nums2 = nums+nums
        stack  = []
        greater = defaultdict(lambda : -1)
        for i in range(len(nums2)):

            while stack and nums2[stack[-1]]<nums2[i]:
                greater[stack.pop()] = nums2[i]

            stack.append(i)
        
        return [greater[e] for e in range(len(nums))]