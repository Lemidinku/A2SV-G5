class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        matrix_sum = 0
        for i in range(n):
            matrix_sum += mat[i][i]

        row = 0
        col = n-1
        while row<n:
            matrix_sum += mat[row][col]
            row+=1
            col-=1
        
        if n%2:
            matrix_sum -= mat[n//2][n//2]
        return matrix_sum