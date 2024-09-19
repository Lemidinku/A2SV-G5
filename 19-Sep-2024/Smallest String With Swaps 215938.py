# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        def find(i):
            if parent[i]==i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
             
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX!=parentY:
                parent[parentY] = parentX

        for a,b in pairs:
            union(a,b)
            
        groups =defaultdict(list)
        for i in range(n):
            a = find(i)
            heappush(groups[a], s[i])
        
        ans = ""
        for i in range(n):
            a = find(i)
            ans += heappop(groups[a])

        return ans
        

