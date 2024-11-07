# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = list(map(neg, nums))
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            num = -heapq.heappop(nums)
            score += num
            heapq.heappush(nums,-math.ceil(num/3))
        return score