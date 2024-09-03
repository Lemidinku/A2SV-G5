# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = []

        for i in range(len(original)):
            row = i//n
            col = i%n
            if row>=m or col >= n: return []
            if col ==0:matrix.append([])
            matrix[-1].append(original[i])

        if len(matrix[-1]) < n or len(matrix) <  m: return []
        return matrix