# Problem: E - Weighted Cycle Search - https://codeforces.com/gym/520688/problem/E

from collections import Counter, defaultdict, deque
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    parent = [i for i in range(n+1)]
    rank = [0 for i in range(n+1)]
    def find(i):
        if parent[i]==i:
            return i
        parent[i] = parent[parent[i]] = find(parent[parent[i]])
        return parent[i]
            
    def union(x, y):
        parentX = find(x)
        parentY = find(y)
        if rank[parentX]<rank[parentY]:
            parent[parentX] = parentY
        elif rank[parentX]>rank[parentY]:
            parent[parentY] = parentX

        else:
            parent[parentX] = parentY
            rank[parentY]+= 1
    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().split())))

    edges.sort(key=lambda x:-x[2])

    ans = None
    graph = defaultdict(list)
    for u,v,w in edges:
        if find(u)==find(v):
            ans = (u,v,w)
        else:
            union(u,v)
        graph[u].append(v)
        graph[v].append(u)
    start, end, min_weight = ans
    visited = set([start])
    queue = deque([start])
    par = {i:-1 for i in range(n+1)}
    dis = 1
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr==end:
                break
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    if curr == start and neighbour==end: continue
                    visited.add(neighbour)
                    queue.append(neighbour)
                    par[neighbour] = curr
        dis +=1
    v = end
    path = []
    while par[v] != -1:
        path.append(v)
        v = par[v]
    path.append(start)

    print(min_weight, len(path))
    print(*path)




        

