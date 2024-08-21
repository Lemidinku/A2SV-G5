# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            y = find(y)
            x = find(x)
            if x == y:
                return -1
            if members[x] > members[y]:
                parent[y] = parent[x]
                members[x] += members[y]
            else:
                parent[x] = parent[y]
                members[y] += members[x]

        parent = {p: p for p in range(n)}
        members = [1]*n

        for a,b in edges:
            union(a,b)
        
        groups = defaultdict(int)
        for i in range(n):
            groups[find(i)] = members[find(i)]
        canReach = 0
        for val in groups.values():
            canReach += (val*(val-1))//2
        
        return (n*(n-1))//2 - canReach
