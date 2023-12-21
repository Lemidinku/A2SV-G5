class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        max_hourglass = 0
        for r in range(1,m-1):
            for c in range(1,n-1):
                hourglass = grid[r][c]
                hourglass += sum(grid[r-1][c-1:c+2])
                hourglass += sum(grid[r+1][c-1:c+2])

                max_hourglass = max(hourglass, max_hourglass)
        return max_hourglass
