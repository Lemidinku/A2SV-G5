# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n,m = len(points[0]), len(points)

        for i in range(m):
            maxx = 0
            temp = []
            for j in range(n):
                if i>0:  points[i][j] +=  points[i-1][j]
                maxx = max(maxx-1, points[i][j])
                temp.append(maxx)
            maxx = 0
            for j in reversed(range(n)):
                maxx = max(maxx-1, points[i][j])
                temp[j] = max(maxx, temp[j])
            points[i] = temp[::]
                

        return max(points[-1])
            
            
                