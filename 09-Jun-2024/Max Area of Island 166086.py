# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dir = [(0,1), (0,-1), (-1,0), (1,0)]
        visited = set()
        def inbound(row, col):
            return 0<=row<n and 0<=col<m


        def dfs(curr):
            visited.add(curr)
            row,col =curr
            area = 1
            for x,y in dir:
                if  inbound(row+x,col+y) and grid[row+x][col+y]==1 and (row+x,col+y) not in visited:
                    area +=dfs((row+x,col+y))
            return area


        max_area = 0
        for i in range(n):
            for j in range(m):
                if  grid[i][j]==1 and (i,j) not in visited:
                    max_area = max(max_area,dfs((i,j)))
        return max_area