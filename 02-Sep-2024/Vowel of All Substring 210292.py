# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i in range(n):
            if word[i] in ('a', "e", "i", "o", "u"):
                ans += (i+1)*(n-i)

        return ans