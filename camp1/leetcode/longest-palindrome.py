from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        leng = 0
        for letter in count.keys():
            if count[letter]%2==0:
                leng += count[letter] 
            else:
                leng += count[letter]-1
        if len(s)>leng: leng+=1
        return leng