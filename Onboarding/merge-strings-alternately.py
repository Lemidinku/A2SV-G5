class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn  = 1
        i =0
        j =0
        new_word = ""
        while i<len(word1) and j<len(word2):
            if turn:
                new_word +=  word1[i]
                i+=1
                turn = 0
            else:
                new_word +=  word2[j]
                j+=1
                turn = 1
                
        # only one of these line will add characters to the new_word
        new_word += word1[i:]
        new_word += word2[j:]
        return new_word
