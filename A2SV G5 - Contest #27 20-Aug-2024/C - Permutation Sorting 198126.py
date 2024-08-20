# Problem: C - Permutation Sorting - https://codeforces.com/gym/538762/problem/C

t = int(input())
for _ in range(t):
    n  = int(input())
    arr = list(map(int, input().split()))

    nums = {arr[i]:i for i in range(n)}

    correct = 0

    for i in range(1,n):
        if nums[i] < nums[i+1]:
            correct += 1
    print(n-1-correct)