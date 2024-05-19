n,k = map(int, input().split())
arr = list(map(int, input().split()))


dp = [float('inf')]*n
dp[0] = 0

for i in range(1,n):
    for j in range(k+1):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(arr[i]-arr[i-j]))
print(dp[-1])
