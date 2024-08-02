# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(1,n):
                if matrix[r][c] and  (matrix[r][c-1]==0 or matrix[r][c-1]=='*'):
                    matrix[r][c] ='*'
            for c in reversed(range(0,n-1)):
                if matrix[r][c] and (matrix[r][c+1]==0 or matrix[r][c+1]=='*'):
                    matrix[r][c] ='*'
        for c in range(n):
            for r in range(1,m):
                if matrix[r][c] and  (matrix[r-1][c]==0 or matrix[r-1][c]=='#'):
                    matrix[r][c] ='#'
            for r in reversed(range(0,m-1)):
                if matrix[r][c] and (matrix[r+1][c]==0 or matrix[r+1][c]=='#'):
                    matrix[r][c] ='#'
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c]=='*' or matrix[r][c]=='#':
                    matrix[r][c]= 0
