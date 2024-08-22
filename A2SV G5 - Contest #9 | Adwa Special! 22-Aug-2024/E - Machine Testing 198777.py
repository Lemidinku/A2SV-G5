# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E

# monotonic Stack
import math
t = int(input())
for _ in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    powers =  list(map(int, input().split()))
    if len(health)==1:
        print(0)
        continue
    time = [0]*n
    stack = [0, 1]
    time[0] = float("inf")
    time[1] = math.ceil(health[1]/powers[0])
    for gun in range(2,n):
 
        while stack and health[gun]>=(time[stack[-1]]-time[gun])*powers[stack[-1]]:
            health[gun]-=(time[stack[-1]]-time[gun])*powers[stack[-1]]
            time[gun] += time[stack[-1]]-time[gun]
            stack.pop()
        
        if health[gun]>0:
            time[gun] += math.ceil(health[gun]/powers[stack[-1]])
        stack.append(gun)
    # print(time)
    
    print(max(time[1:]))