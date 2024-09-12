# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            allFound = True
            for letter in word:
                if letter not in allowed:
                    allFound = False
            if allFound: count+=1
        return count
