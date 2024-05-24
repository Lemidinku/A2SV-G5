# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26)]
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.is_end = True

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            ind = ord(char)-ord("a")
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True

    def search(self, word: str) -> bool:
        root_word = ""
        curr = self.root
        for char in word:
            ind = ord(char)-ord("a")
            if not curr.children[ind]:
                return ""
            root_word += char
            if curr.children[ind].is_end:
                return root_word
            curr = curr.children[ind]
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        ans = []
        for word in sentence.split(' '):
            root_word = trie.search(word)
            if root_word: ans.append(root_word)
            else: ans.append(word)

        return " ".join(ans)