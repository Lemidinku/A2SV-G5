class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                count,prev  = freq[nums[i]]
                
                result[i] += (i-prev)*count 
                if i>0: result[i] += result[prev]
                freq[nums[i]] = (count+1, i)
            else:
                freq[nums[i]] = (1,i)

        freq = {}
        arr = [0]*len(nums)
        for i in range(len(nums)-1, -1,-1):
            if nums[i] in freq:
                count,prev  = freq[nums[i]]
                
                arr[i] += (prev-i)*count 
                if i<len(nums)-1 : arr[i] += arr[prev]
                freq[nums[i]] = (count+1, i)
            else:
                freq[nums[i]] = (1,i)
        for i in range(len(result)):
            result[i] += arr[i]
        return result


            

