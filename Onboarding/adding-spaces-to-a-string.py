class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = ""
        j = 0
        for i in range(len(s)):
            if j<len(spaces) and i==spaces[j]  :
                new_str += " "
                j+=1
            new_str+=s[i]
        return new_str
