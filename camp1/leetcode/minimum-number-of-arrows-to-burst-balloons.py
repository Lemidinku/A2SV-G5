class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        
        arrow_pos = points[0][1]
        arrows_needed = 1
        for x1, x2 in points[1:]:
            if not(x1<=arrow_pos<=x2): # not in between 
                arrows_needed += 1
                arrow_pos = x2
        return arrows_needed

