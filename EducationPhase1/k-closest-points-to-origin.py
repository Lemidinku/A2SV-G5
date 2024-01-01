import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return math.sqrt(point[0]**2 + point[1]**2)
        points.sort(key = lambda point : distance(point))
        print(points)
        return points[:k]

10, 8


26, 20, 18
        

