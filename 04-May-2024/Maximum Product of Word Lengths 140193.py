# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        def hasCommon(word1, word2):
            return word1&word2!=0
        
        def change_to_bits(word):
            bits = 0
            for char in word:
                val = ord(char)-ord("a")
                bits |= (1<<val)
            return bits
        words = [(len(word), change_to_bits(word)) for word in words]
        maxx = 0
        for i in range(n):
            for j in range(n):
                if i!=j:
                    len1, word1 = words[i]
                    len2,word2 = words[j]
                    if not hasCommon(word1, word2):
                        maxx = max(maxx, len1*len2)
        return maxx
