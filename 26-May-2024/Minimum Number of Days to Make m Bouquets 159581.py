# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def possible_bouquets(today):
            bouquets_made =0
            left = 0
            right = 0
            while right<n:
                if bloomDay[left] > today:
                    left +=1
                    right  = left
                else:
                    if  bloomDay[right] > today:
                        bouquets_made += (right-left)//k
                        right+=1
                        left=right
                    else:
                        right +=1
            bouquets_made += (n-left)//k
            return bouquets_made
        

        left = 0
        right = max(bloomDay)
        while left<=right:
            mid = left + (right-left)//2

            if possible_bouquets(mid) >= m:
                right = mid-1
            else:
                left = mid+1
        
        return left if left <= max(bloomDay) else -1
            


                



