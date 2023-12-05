class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time  = 0
        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]

            min_time += max( abs(x1-x2), abs(y1-y2))
        return min_time