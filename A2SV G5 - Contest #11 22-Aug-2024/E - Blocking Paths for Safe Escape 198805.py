# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E


    

import sys, threading
input = lambda: sys.stdin.readline().strip()
def main():
    t = int(input())
    for b in range(t):
        m,n = map(int, input().split())
        grid = [list(input()) for _ in range(m)]
        # print(grid)

        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
        visited = set()
        def dfs(i,j):
            visited.add((i,j))

            notAllowed = False
            for x,y in dir:
                if inbound(i+x, y+j) and grid[i+x][y+j]!="#" and (i+x, y+j) not in visited:
                    if grid[i+x][y+j]=="B" :
                        notAllowed = True
                        break
            if notAllowed:
                return 0
            count =0
            if grid[i][j] == "G":

                count = 1
            for x,y in dir:
                if inbound(i+x, y+j) and grid[i+x][y+j]!="#" and (i+x, y+j) not in visited:
                    if grid[i+x][y+j]=="B" :
                        break
                    count += dfs(i+x, y+j)
            return count
        count =dfs(m-1, n-1)
        
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "G":
                    c += 1

        if c==count:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()