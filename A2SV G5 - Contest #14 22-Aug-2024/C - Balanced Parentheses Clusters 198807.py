# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    n *=2
    word = input()
    count = 0
    for i in range(n-1):
        if word[i]==word[i+1]=="(":
            count +=1
    print(count+1)
