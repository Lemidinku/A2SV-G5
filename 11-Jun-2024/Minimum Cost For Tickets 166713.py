# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        valid_for = [1, 7, 30]
        n = len(days)
        @cache
        def backtrack(i, ends):
            if i>= n:
                return 0


            money_needed = float('inf')
            if days[i]>=ends:
                for x in range(3):
                    money_needed = min(money_needed,backtrack(i+1, days[i]+valid_for[x])+ costs[x]) 
            else:
                money_needed = min(money_needed,backtrack(i+1, ends))
               
            return money_needed 

        return backtrack(0,0)
