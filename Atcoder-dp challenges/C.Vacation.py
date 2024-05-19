n  = int(input())
days = []
for _ in range(n):
    days.append(list(map(int, input().split())))


dp = [[0]*3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = days[0][0], days[0][1], days[0][2]


for day in range(1,n):
    for activity in range(3):
        dp[day][activity] = 0
        for j in range(3):
            if j != activity:
                dp[day][activity] = max(dp[day][activity],dp[day-1][j] +days[day][activity])

print(max(dp[-1]))