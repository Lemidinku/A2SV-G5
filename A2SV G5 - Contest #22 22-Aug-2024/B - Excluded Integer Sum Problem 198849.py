# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())

    def possible():
        if x!=1:
            print("YES")
            print(n)
            print(*[1]*n)
        else:
            if k==1:
                print("NO")
                return
            if k==2:
                if n%2:
                    print("NO")
                else:
                    print("YES")
                    print(n//2)
                    print(*[2]*(n//2))
            else:
                print("YES")
                if not n%2:
                    print(n//2)
                    print(*[2]*(n//2))
                else:
                    print(n//2)
                    print(*([2]*(n//2-1)+[3]))

    possible()


