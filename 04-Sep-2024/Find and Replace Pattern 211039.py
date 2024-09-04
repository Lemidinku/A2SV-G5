# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def hasPattern(word, pattern):
            mapped = dict()
            used = set()
            for i in range(len(word)):
                if word=="ccc": print(word[i], pattern[i])
                if word[i] not in mapped:
                    if pattern[i] in used: return False
                    mapped[word[i]] = pattern[i]
                    used.add(pattern[i])
                elif mapped[word[i]] != pattern[i]:
                    return False
            return True
        ans = []
        for word in words:
            if hasPattern(word, pattern):
                ans.append(word)
        return ans
        
