# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

n,s = map(int, input().split())
if s==0:
    if n==1:
        print("0 0")
    else:
        print("-1 -1")
    quit()
s2 = s
# greater num
large = 0
for i in reversed(range(n)):
    dig = min(s,9)
    s -= dig
    val = dig*(10**i)
    large += val
if s:
    print("-1 -1")
    quit()
s = s2
small = 0
for i in range(n):
    dig = min(s, 9)
    val = dig*(10**i)
    small += val
    s -= dig
if s:
    print("-1 -1")
    quit()
if small//(10**(n-1))<1:
    for i in reversed(range(n)):
        if small//(10**i)>=1:
            small -= (10**i)
            break
    small += (10**(n-1))

    
if small<0 or large<0 :
    print("-1 -1")
else:
    print(small, large)
