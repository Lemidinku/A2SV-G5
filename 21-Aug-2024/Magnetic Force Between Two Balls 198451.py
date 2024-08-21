# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def isValid(arr, dis,m):
            prev = arr[0]
            canBePlaced = 1
            for i in range(1, len(arr)):
                if arr[i]-prev >= dis:
                    canBePlaced += 1
                    prev = arr[i]
            return canBePlaced>=m
        left , right = 1, position[-1]
        while left<=right:
            mid = left + (right-left)//2
            if isValid(position,mid,m):
                left = mid+1
            else:
                right = mid-1
        return right

        

                    
