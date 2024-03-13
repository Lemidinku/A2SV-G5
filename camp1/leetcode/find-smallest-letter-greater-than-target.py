from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x = bisect_right(letters, target)
        return letters[x%len(letters)]
        