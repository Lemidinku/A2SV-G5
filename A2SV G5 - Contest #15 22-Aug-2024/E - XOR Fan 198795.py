# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

t = int(input())
for _ in range(t):
    n  = int(input())
    nums = list(map(int, input().split()))
    s = input()

    prefix = [0]
    for number in nums:
        prefix.append(prefix[-1] ^ number)
    zeros = 0
    ones = 0
    for i in range(n):
        if s[i]=="1":
            ones ^= nums[i]
        else:
            zeros ^= nums[i]
    
    q = int(input())
    ans = []
    for _ in range(q):
        ops = list(map(int, input().split()))
        if ops[0]==1:
            _, left, right = ops
            rang = prefix[right]^prefix[left-1]
            zeros ^= rang
            ones ^= rang
        else:
            _, g = ops
            if g:
                ans.append(ones)
            else:
                ans.append(zeros)
    print(*ans)


