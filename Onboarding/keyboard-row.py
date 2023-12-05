class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows_of_letters = {}

        # constructing a dict that maps letters with their rows
        for char in "qwertyuiop":
            rows_of_letters[char] = 0
        for char in "asdfghjkl":
            rows_of_letters[char] = 1
        for char in "zxcvbnm":
            rows_of_letters[char] = 2

        possible_words = []
        for word in words:
            can_write = True
            for i in range(len(word)-1):
                letter1, letter2  = word[i].lower(), word[i+1].lower()
                if rows_of_letters[letter1] != rows_of_letters[letter2]:
                    can_write = False
                    break
            if can_write: possible_words.append(word)
        return possible_words


