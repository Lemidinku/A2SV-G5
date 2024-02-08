class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        request_arr = [0]*(n+1)

        for start,end in requests:
            request_arr[start] += 1
            request_arr[end+1] -=1
        
        for i in range(1,len(request_arr)):
            request_arr[i] += request_arr[i-1]

        arr = [i for i in range(n)]
        arr.sort(key=lambda i:-request_arr[i])
        nums.sort(reverse=True)

        new_arr = [0]*n

        for ind,val in zip(arr,nums):
            new_arr[ind]= val

        
        
        for i in range(1,n):
            new_arr[i] += new_arr[i-1]
        new_arr.insert(0,0)
        
        result = 0
        for l,r in requests:
            result += new_arr[r+1]-new_arr[l]
        return result%(10**9+7)


            
