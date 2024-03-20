class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix[0]), len(matrix)
        left =0
        right = (n*m)-1
        while left<=right:
            mid = left+(right-left)//2
            r,c = mid//n, mid%n
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                right = mid-1
            else:
                left = mid+1

        return False