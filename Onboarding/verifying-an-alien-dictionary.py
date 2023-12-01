class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order  = { b:a for  a,b in enumerate(order)}
        def is_less(word1, word2):
            i = 0
            while  i<len(word1) and i<len(word2):
                if order[word1[i]]> order[word2[i]]:
                    return False
                elif order[word1[i]] < order[word2[i]]:
                    return True
                i+=1
            
            return len(word1) <= len(word2)

        for i in range(len(words)-1):
            if not is_less(words[i], words[i+1]):
                return False
        return True
        