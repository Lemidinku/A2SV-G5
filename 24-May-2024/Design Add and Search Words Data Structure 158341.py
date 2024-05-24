# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root  = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            ind = ord(char)-ord("a")
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True


    def search(self, word: str) -> bool:
        n = len(word)
        def search_word(i, curr):
            found = False
            if i==n:
                return curr.is_end
            char = word[i]
            if char==".":
                for ind in range(26):
                    if curr.children[ind]:
                        found |=search_word(i+1, curr.children[ind])
            else:
                ind = ord(char)-ord("a")
                if curr.children[ind]:
                    found |= search_word(i+1, curr.children[ind])
            return found
        return search_word(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)