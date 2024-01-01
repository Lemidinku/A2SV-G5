class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles.sort(reverse=True)
        count = 0
        for i in range(1,2*n, 2):
            count += piles[i]

        return count