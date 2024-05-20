# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = defaultdict(lambda : float('inf'))
        dp[(0,0)]  = triangle[0][0]
        for row in range(1,m):
            for col in range(len(triangle[row])):
                ans = dp[(row, col)]
                if col>0:
                    ans = dp[(row-1, col-1)] + triangle[row][col]
                if col < len(triangle[row-1]):
                    ans = min(ans, dp[(row-1, col)]+ triangle[row][col])
                dp[(row, col)] = ans
        min_path = float("inf")
        for i in range(len(triangle[-1])):
            min_path = min(min_path, dp[(m-1, i)])
        return min_path