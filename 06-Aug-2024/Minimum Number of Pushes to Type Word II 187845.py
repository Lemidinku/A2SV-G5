# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        
        letters = list(count.keys())
        letters.sort(key = lambda x: -count[x])
        
        
        press = 0
        for i in range(len(letters)):
            press += (i//8 + 1)*count[letters[i]]
        return press
            