# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

n =int(input())
parent = [i for i in range(n+1)]
ans = [[i] for i in range(n+1)]
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
        ans[parentY].extend(ans[parentX])
    elif rank[parentX]>rank[parentY]:
        parent[parentY] = parentX
        ans[parentX].extend(ans[parentY])

    else:
        parent[parentX] = parentY
        ans[parentY].extend(ans[parentX])
        rank[parentY]+= 1

for _ in range(n-1):
    a,b = map(int, input().split())
    if find(a)!=find(b):
        union(a,b)
result = []
for arr in ans:
    if len(arr)==n:
        result = arr
print(*result)
