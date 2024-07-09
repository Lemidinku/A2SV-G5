# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-x for x in stones]
        heapq.heapify(arr)


        while len(arr)>1:
            stone1 = -heapq.heappop(arr)
            stone2 = -heapq.heappop(arr)
            if stone1!=stone2:
                heapq.heappush(arr,-abs(stone1-stone2))
        if arr: return -arr[0]
        return 0
