# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        minutes = [int(x[:2])*60 +int(x[3:]) for x in timePoints]
        minutes.sort()
        minn = float('inf')
        for i in range(n-1):
            diff = minutes[i+1]-minutes[i]
            minn = min(minn, diff)

        diff = 24*60-minutes[-1]+minutes[0]
        minn = min(minn, diff)

        return minn