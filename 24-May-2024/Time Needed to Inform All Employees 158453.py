# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i]!=-1:
                graph[manager[i]].append(i)
        def dfs(curr):
            time = 0
            for subord in graph[curr]:
                time  = max(time, informTime[curr] + dfs(subord))
            return time
        return dfs(headID)