# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Initialization
        prev = [float('inf')] * n
        prev[src] = 0
        # Perform N-1 iterations (where N is the number of nodes)
        for i in range(k+1):
            curr = prev[:]
            
            # Relax all edges
            for u, v, w in flights:
                curr[v] = min(curr[v], prev[u]+w)
            # Swap the arrays, prev now points to curr
            prev = curr[:]
        return prev[dst] if prev[dst] < float('inf') else -1
