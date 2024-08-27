# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, x = map(int, input().split())
arr = list(map(int, input().split()))


def solve():
    curr = 1
    while curr < x:
        curr += arr[curr-1]
        if curr == x:
            print("YES")
            return
    print("NO")


solve()


    