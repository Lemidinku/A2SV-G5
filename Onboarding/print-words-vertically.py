class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = list(s.split())
        maxx = 0
        for word in words:
            maxx = max(maxx, len(word))
        vert_words = []
        for i in range(maxx):
            vert_word = ""
            for word in words:
                if i<len(word):
                    vert_word += word[i]
                else:
                    vert_word += " "
            vert_words.append(vert_word.rstrip())
        return vert_words



