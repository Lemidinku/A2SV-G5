class Solution:
    def freqAlphabets(self, s: str) -> str:

        result  = ""
        i = 0
        while i < len(s):
            if i+2<len(s) and  s[i+2] == "#":
                char = chr(int(s[i:i+2])+96)
                result += char
                i+=3
            else:
                char = chr(int(s[i])+96)
                result += char
                i+=1



        return result

