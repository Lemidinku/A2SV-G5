class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def canHeat(radius):
            heated = set()
            j = i= 0
            while i<len(houses) and j<len(heaters):
                if heaters[j]<=houses[i]:
                    if houses[i]-heaters[j] <= radius:
                        heated.add(i)
                    else:
                        j+=1
                        continue
                i+=1
            j = len(heaters)-1
            i= len(houses)-1
            while i>=0 and j>=0:
                if heaters[j]>=houses[i]:
                    if heaters[j]-houses[i]<= radius:
                        heated.add(i)
                    else:
                        j-=1
                        continue
                i-=1
            return len(heated)==len(houses)
        def solve():
            left = 0
            right = max(houses[-1],heaters[-1])-min(houses[0], heaters[0])//len(heaters)
            while left<=right:
                mid = left + (right-left)//2
                if canHeat(mid):
                    right = mid-1
                else:
                    left = mid+1

            return left
        
        return solve()

        

                    
                    


