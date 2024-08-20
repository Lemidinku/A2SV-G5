# Problem: A - Split the Set - https://codeforces.com/gym/538762/problem/A

t = int(input())
for _ in range(t):
    n  = int(input())
    arr = list(map(int, input().split()))

    odds = 0
    evens  =0
    for a in arr:
        if a%2:
            odds+=1
        else: evens +=1
    
    if odds >= n and evens >= n:
        print('Yes')
    else:
        print("No")