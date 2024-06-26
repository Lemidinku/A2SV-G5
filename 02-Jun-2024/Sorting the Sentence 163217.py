# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        s.sort(key= lambda x: x[-1])

        s = [ word[:-1] for word in s]

        return " ".join(s)
        
