class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_sum = sum(cardPoints[:k])

        max_score = window_sum

        right = n-1
        left = k-1

        while left>=0:
            window_sum += cardPoints[right]
            window_sum -= cardPoints[left]
            max_score = max(max_score, window_sum)
            left-=1
            right-=1
        return max_score