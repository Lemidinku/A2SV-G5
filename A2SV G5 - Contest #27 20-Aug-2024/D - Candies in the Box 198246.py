# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

import math
n  = int(input())
def eatsHalf(n,k):
    initial = n
    value =0
    turn = 0
    while n:
        if not turn:
            value += min(n,k)
            n -= min(n,k)
        else:
            n -= (n//10)
        turn  = 1-turn
    return 2*value >= initial
 
left, right = 1, n
while left <= right:
    mid = left + (right-left)//2
    if eatsHalf(n,mid):
        right = mid-1
    else:
        left = mid+1
print(left)
 