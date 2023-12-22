class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3: return False
        i  = 0
        while i<n-1 and arr[i] < arr[i+1]:
            if arr[i] == arr[i+1]:
                return False
            i+=1
        if i==n-1: return False


        j  = n-1
        while j>0 and arr[j-1] > arr[j]:
            if arr[j-1] == arr[j]:
                return False
            j-=1
        if j==0: return False


        return i == j

