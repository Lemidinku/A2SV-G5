class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0]*n

        for first, last, seats in bookings:
            pref[first-1] += seats
            if last<n:
                pref[last] -= seats
        
        for i in range(1,n):
            pref[i] += pref[i-1]
        return pref