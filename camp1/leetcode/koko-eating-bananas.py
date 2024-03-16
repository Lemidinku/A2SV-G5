class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def canEat(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)

            return hours<=h

        left = 1
        right = max(piles)

        while left<=right:
            mid = left + (right-left)//2

            if canEat(mid):
                right = mid-1
            else:
                left = mid+1
        return left

        