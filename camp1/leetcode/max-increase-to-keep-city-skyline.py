class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_maxes = [0]*n
        for r in range(n):
            row_maxes[r]= max(grid[r])

        col_maxes = [0]*n

        for c in range(n):
            maxx = 0
            for r in range(n):
                maxx = max(maxx, grid[r][c])
            col_maxes[c] = maxx


        result = 0
        for r in range(n):
            for c in range(n):

                result += min(row_maxes[r], col_maxes[c])-grid[r][c]
        
        return result
