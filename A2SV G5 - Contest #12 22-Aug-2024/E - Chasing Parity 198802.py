# Problem: E - Chasing Parity - https://codeforces.com/gym/517685/problem/E

from collections import Counter, defaultdict, deque

n =int(input())
arr = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(n):
    if i+arr[i] < n:
        graph[i+arr[i]].append(i)
    if i-arr[i] >=0:
        graph[i-arr[i]].append(i)


result = [-1]*n

def bfs(parity):
    queue  = deque()
    visited  = set()
    for i in range(n):
        if arr[i]%2==parity:
            visited.add(i)
            queue.append(i)
    dis = 0
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            if arr[curr]%2!= parity:
                result[curr] = dis

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        dis +=1
bfs(0)
bfs(1)
print(*result)

