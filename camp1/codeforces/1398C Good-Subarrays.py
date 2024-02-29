from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, list(input())))

    freq= defaultdict(int)
    freq[0] = 1
    count = 0
    summ = 0
    for i,num in enumerate(nums):
        summ += num
        count += freq[summ-i - 1]
        freq[summ-i - 1]  +=1



    print(count)