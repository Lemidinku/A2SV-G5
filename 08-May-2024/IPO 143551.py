# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        capital = [(capital[i],i) for i in range(len(capital))]
        capital.sort()
        possible_jobs = []
        ind = 0
        for _ in range(k):
            while ind<len(capital) and capital[ind][0]<=w:
                heappush(possible_jobs, -profits[capital[ind][1]])
                ind +=1
            if possible_jobs:
                w -= heappop(possible_jobs)
        return w
            
        

            






