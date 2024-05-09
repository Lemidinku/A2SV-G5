# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiency = [(efficiency[i],i) for i in range(len(efficiency))]
        efficiency.sort(reverse = True)
        speed_heap = []
        curr_sum = 0
        ans = 0
        for i in range(k-1):
            heappush(speed_heap, speed[efficiency[i][1]])
            curr_sum += speed[efficiency[i][1]]
            ans = max(ans, efficiency[i][0]*curr_sum)

        for i in range(k-1,n):
            curr_speed = speed[efficiency[i][1]]
            performance = (curr_sum + curr_speed)*efficiency[i][0]
            ans = max(performance, ans)
            if speed_heap and speed_heap[0]<curr_speed:
                replaced = heappop(speed_heap)
                heappush(speed_heap, speed[efficiency[i][1]])
                curr_sum += speed[efficiency[i][1]] - replaced


        return ans%(10**9+7)

            

