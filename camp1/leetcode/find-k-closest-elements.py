class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        diffs = sorted(arr, key=lambda a:abs(a-x))

        return sorted(diffs[:k])