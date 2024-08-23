# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)
        top = bottom = 0

        result = []
        while top<n and bottom<m:
            a1,b1 = firstList[top]
            a2,b2 = secondList[bottom]

            if max(a1,a2)<=min(b1,b2):
                result.append([max(a1,a2), min(b1,b2)])
                
            if b1<b2:
                top+=1
            else:
                bottom +=1
            
        return result







        