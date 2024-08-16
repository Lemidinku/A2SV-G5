# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    lowest_1 =  lowest_2 = float('inf')
    from collections import defaultdict
    students = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest_1:
            lowest_2 = lowest_1
            lowest_1 = score
        elif score > lowest_1 and score < lowest_2:
            lowest_2 = score
        if score in  students:
            students[score].append(name)
        else:
            students[score] = [name]
    
    ans = students[lowest_2]
    ans.sort()
    for name in ans:
        print(name)