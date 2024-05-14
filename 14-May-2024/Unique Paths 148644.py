# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = {}

        def dfs(row, col):
            if row==m-1 and col==n-1:
                return 1

            if (row,col) in self.cache: 
                return self.cache[(row,col)]
            ways = 0
            for x,y in [(1,0), [0,1]]:
                if 0<=row+x<m and 0<=col+y<n:
                    ways +=dfs(row+x, col+y)
            self.cache[(row,col)] = ways
            return ways


        return dfs(0,0)
                    