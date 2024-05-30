# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        n = len(values)
        @cache
        def dp(left, right):
            if right-left<2: return 0

            minn = float('inf')
            for vertix in range(left+1, right):
                choice_score = values[left]*values[vertix]*values[right] + dp(left,vertix) + dp(vertix, right)
                minn = min(choice_score, minn)

            return minn
        
        return dp(0,n-1)