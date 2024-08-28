# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        min_1, min_2 = -1, -1
        max_1, max_2 = -1, -1
        arrays.append([float('inf'), float('-inf')])

        for i in range(len(arrays)-1):
            array = arrays[i]
            if array[0] < arrays[min_1][0]:
                min_2, min_1 = min_1, i
            elif array[0] <arrays[min_2][0]:
                min_2 = i
            if array[-1] > arrays[max_1][-1]:
                max_2, max_1 = max_1, i
            elif array[-1] > arrays[max_2][-1]:
                max_2 = i
            
        ans =0
        if min_1 != max_1: ans = max(ans, arrays[max_1][-1]-arrays[min_1][0])
        if min_1 != max_2: ans = max(ans,  arrays[max_1][-1]-arrays[min_2][0])
        if min_2 != max_1: ans = max(ans,  arrays[max_2][-1]-arrays[min_1][0])
        if min_2 != max_2: ans = max(ans,  arrays[max_2][-1]-arrays[min_2][0])


        return ans
        




        