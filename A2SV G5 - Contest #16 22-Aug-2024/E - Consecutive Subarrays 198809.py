# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E


n,k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]
for number in arr[::-1]:
    prefix_sum.append(prefix_sum[-1] + number)
prefix_sum = prefix_sum[::-1]
prefix_sum.pop()

ans = prefix_sum[0]
prefix_sum.pop(0)
prefix_sum.sort(reverse=True)
k-=1
i = 0
while k:
    ans += prefix_sum[i]
    k-=1
    i+=1

print(ans)




