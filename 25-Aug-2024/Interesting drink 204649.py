# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

from bisect import bisect_right
n  = int(input())
arr = list(map(int, input().split()))
arr.sort()
q = int(input())
for i in range(q):
    x = int(input())
    print(bisect_right(arr, x))
    