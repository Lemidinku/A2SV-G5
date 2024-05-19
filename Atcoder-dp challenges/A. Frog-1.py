n = int(input())
arr = list(map(int, input().split()))


dp = [float('inf')]*n
dp[0] = 0
dp[1] = abs(arr[0]-arr[1])

for i in range(1,n):
    dp[i] = min(
        dp[i-1] + abs(arr[i]-arr[i-1]),
        dp[i-2] + abs(arr[i]-arr[i-2])

    )
print(dp[-1])
