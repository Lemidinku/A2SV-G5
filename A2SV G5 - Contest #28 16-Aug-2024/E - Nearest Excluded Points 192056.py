# Problem: E - Nearest Excluded Points - https://codeforces.com/gym/540354/problem/E

n = int(input())

arr = list(map(int, input().split()))
nums = set(arr)

def solve():
    for p in range(31):
        for i in range(n):
            if arr[i] + (1<<p) in nums and arr[i] - (1<<p) in nums:
                print(3)
                print(arr[i] - (1<<p), arr[i], arr[i] + (1<<p))
                return
    for p in range(31):
        for i in range(n):
            if arr[i] + (1<<p) in nums:
                print(2)
                print(arr[i], arr[i] + (1<<p))
                return
    print(1)
    print(arr[0])


if __name__ == "__main__":
    solve()
            
