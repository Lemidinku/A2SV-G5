# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n,m = len(grid1[0]), len(grid1)
        dir = {(0,1), (1, 0), (-1, 0), (0,-1)}

        def inBound(r,c):
            return 0<=r<m and 0<=c<n and grid2[r][c]
                    
        def dfs(row,col):
            grid2[row][col]=0
            sub_island = True
            if not grid1[row][col]:
                sub_island = False
            for x,y in dir:
                if inBound(row+x, col+y):
                    sub_island &= dfs(row+x, col+y)
            return sub_island
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    if dfs(i,j):
                        ans +=1
        
        return ans