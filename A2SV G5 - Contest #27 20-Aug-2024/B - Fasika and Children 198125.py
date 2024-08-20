# Problem: B - Fasika and Children - https://codeforces.com/gym/538762/problem/B

n, m = map(int, input().split())
import math
arr = list(map(int, input().split()))

nums = [math.ceil(a/m) for a in arr]

ans = 0
for i in range(n):
    if nums[i] >= nums[ans]:
        ans = i
print(ans+1)

