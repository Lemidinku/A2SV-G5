class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for row in range(n-1):
            for col in range(row+1,n):
                matrix[row][col], matrix[col][row] = matrix[col][row] ,matrix[row][col]


        for i in range(n):
            left = 0
            right = n-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left+=1
                right -=1
        

        
        