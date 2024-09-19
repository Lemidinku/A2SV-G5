# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre = [0]
        curr = 0
        for i in range(len(arr)):
            curr ^=arr[i]
            pre.append(curr)
        result = []
        for left, right in queries:
            result.append(pre[left]^pre[right+1])

        return result