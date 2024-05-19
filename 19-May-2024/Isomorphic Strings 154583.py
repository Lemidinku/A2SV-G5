# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                if table[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in table.values(): return False
                table[s[i]] = t[i]
        return True
            
