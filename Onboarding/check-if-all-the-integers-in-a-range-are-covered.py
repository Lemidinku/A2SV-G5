class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()    
        for  inter in ranges:
            for i in range(inter[0], inter[1]+1):
                covered.add(i)

        for num in range(left, right+1):
            if num not in covered:
                return False
        return True