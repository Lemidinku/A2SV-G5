class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def getPascal(n):
            if n == 0:
                return [1]
            if n==1:
                return [1,1]
            arr = getPascal(n-1)
            new_arr = [1]
            for i in range(len(arr)-1):
                new_arr.append(arr[i]+arr[i+1])
            new_arr.append(1)

            return new_arr

        return getPascal(rowIndex)
