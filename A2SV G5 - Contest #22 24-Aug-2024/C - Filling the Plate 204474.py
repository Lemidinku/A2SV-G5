# Problem: C - Filling the Plate - https://codeforces.com/gym/531455/problem/C

import sys
k, n, m = map(int, input().split())
block = []
input()
for _ in range(k):
    grid = [list(input()) for _ in range(n)]
    block.append(grid)
    input()

dir = [(1,0), (0,1), (-1,0), (0,-1)]

visited = set()

def fill(r, c, layer):
    ans = 1
    block[layer][r][c] = "#"
    for a, b in dir:
        x, y = r+a, c+b
        if 0 <= x < n and 0 <= y < m and block[layer][x][y] == '.':
            ans += fill(x, y, layer)
    if layer < k-1 and block[layer+1][r][c] == '.':
        ans += fill(r, c, layer+1)
    if layer >0 and block[layer-1][r][c] == '.':
        ans += fill(r, c, layer-1)

    
    return ans
a, b = map(int, input().split())

print(fill(a-1, b-1, 0))




