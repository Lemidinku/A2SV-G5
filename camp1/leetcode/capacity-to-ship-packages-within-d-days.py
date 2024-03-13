class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysTaken(capacity):
            days = 1
            summ =0
            for weight in weights:
                if summ+weight>capacity:
                    summ =0
                    days +=1
                summ+=weight
            return days

        left = max(weights)
        right = sum(weights)

        while left<=right:
            mid = left + (right-left)//2
            daysNeeded = daysTaken(mid)
            if daysNeeded>days:
                left = mid+1
            else:
                right = mid-1
        
        return left

