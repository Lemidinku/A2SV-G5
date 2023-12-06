class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        stack = []
        count = 0
        for num in nums:
            while stack and stack[-1]>num:
                stack.pop()
                count +=1
            stack.append(num)

        stack = []
        count2 = 0
        for num in nums[::-1]:
            while stack and stack[-1]<num:
                stack.pop()
                count2 +=1
            stack.append(num)
        return count<=1 or count2<=1
        




        
