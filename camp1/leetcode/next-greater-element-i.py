class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack  = []
        greater = defaultdict(lambda : -1)
        for num in nums2:

            while stack and stack[-1]<num:
                greater[stack.pop()] = num

            stack.append(num)

        
        result = []
        for n in nums1:
            result.append(greater[n])

        return result
                
