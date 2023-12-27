class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {val:ind for ind,val in enumerate(arr2)}
        k = len(arr1)
        while k>1:
            for i in range(k-1):
                
                if arr1[i] in order and arr1[i+1] in order and order[arr1[i]] > order[arr1[i+1]]:
                   arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
                elif arr1[i] not in order and arr1[i+1] not in order and arr1[i] > arr1[i+1]:
                   arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
                elif arr1[i] not in order and arr1[i+1] in order:
                   arr1[i], arr1[i+1] = arr1[i+1], arr1[i]

            k-=1
        return arr1