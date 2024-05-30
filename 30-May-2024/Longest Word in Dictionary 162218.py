# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/


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
        curr = self.root
        for char in word:
            ind = ord(char)-ord("a")
            if not curr.children[ind] or not curr.children[ind].is_end:
                return False
            curr = curr.children[ind]
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort(key=lambda x: (-len(x),x))
        for word in words:
            if trie.search(word):
                return word
        return ""