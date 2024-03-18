class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        table = {intervals[i][0]:i for i in range(n)}
        arr = [a for a,_ in intervals]
        arr.sort()
        ans = []
        for i in range(n):
            ind = bisect_left(arr, intervals[i][1])

            if ind==n:
                ans.append(-1)
            else:
                ans.append(table[arr[ind]])

        return ans

