# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

from collections import Counter, defaultdict
import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = defaultdict(int)

zeros = 0
for i in range(n):
    if not a[i]: 
        if not b[i]: 
            zeros += 1
    elif not b[i]:
        count[0]+=1
    else:
        g = math.gcd(b[i],a[i])
        x,y = b[i]//g,a[i]//g
        if x*y<0:
            count[(-abs(x), abs(y))]+=1
        else:
            count[(abs(x), abs(y))]+=1

maxx = 0
for b in count.values():
    maxx = max(maxx, b)
print(maxx+zeros)

