class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxx = max(candies)
        result = []
        for a in candies:
            if a+extraCandies>= maxx:
                result.append(True)
            else: result.append(False)
        return result