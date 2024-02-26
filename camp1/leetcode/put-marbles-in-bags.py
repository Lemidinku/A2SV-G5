class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1: return 0
        arr = []
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        return sum(arr[-k+1:]) - sum(arr[:k-1])