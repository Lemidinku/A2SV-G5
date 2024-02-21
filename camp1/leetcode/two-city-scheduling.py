class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x: x[1]-x[0])
        
        min_cost = 0
        for i in range(n//2):
            min_cost += costs[i][1]
        for i in range(n//2,n):
            min_cost += costs[i][0]
        return min_cost