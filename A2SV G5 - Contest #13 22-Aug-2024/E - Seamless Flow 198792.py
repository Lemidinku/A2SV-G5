# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import Counter, defaultdict, deque
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    graph = defaultdict(list)
    incoming = defaultdict(int)
    undirected = set()
    edges = []
    for _ in range(k):
        directed, a, b = map(int, input().split())
        if directed:
            graph[a].append(b)
            incoming[b] += 1
            edges.append((a,b))
        else:
            undirected.add((a,b))
            
    queue = deque()
    topo = []
    for i in range(1, n+1):
        if incoming[i]==0:
            queue.append(i)
            topo.append(i)
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            for neighbour in graph[curr]:
                incoming[neighbour] -=1
                if not incoming[neighbour]:
                    if not incoming[neighbour]:
                        queue.append(neighbour)
                        topo.append(neighbour)
    if len(topo)!=n:
        print("NO")
        continue
    print("YES")
    for a,b in edges:
        print(a,b)
    order = {topo[i]:i for i in range(n)}
    for a,b in undirected:
        if order[a] < order[b]:
            print(a,b)
        else:
            print(b,a)






