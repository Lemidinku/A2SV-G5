class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def rev(start,end):
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end -=1

        n = len(arr)
        result = []
        for i in range(n):
            ind = arr.index(n-i)
            rev(0,ind)
            rev(0,n-i-1)
            result += [ind+1,n-i]

        return result