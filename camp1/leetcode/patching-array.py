class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        summ = 0
        ops = 0
        for i in range(len(nums)):

            while summ < nums[i]:
                if summ+1 == nums[i]:
                    break
                summ+= summ+1
                ops+=1
                if summ>n: break
                
            summ+= nums[i]
            if summ>n: break
 
        
        
        while summ < n:
            summ+= summ+1
            ops+=1
        
        return ops
            
        








    