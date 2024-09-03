# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        from bisect import bisect_right
        n = len(difficulty)
        jobs = [[p,d] for p,d in zip(profit, difficulty)]
        jobs.sort(key=lambda x:x[1])
        
        max_profit = 0
        for i in range(n):
            max_profit = max(jobs[i][0], max_profit)
            jobs[i][0] = max_profit

        difficulty.sort()
        total_profit =0 
        for capacity in worker:
            ind = bisect_right(difficulty, capacity)
            if ind >0:
                total_profit +=  jobs[ind-1][0]
            
        return total_profit