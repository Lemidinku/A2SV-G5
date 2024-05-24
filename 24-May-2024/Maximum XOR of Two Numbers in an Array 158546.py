# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None]*2
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        Trie = lambda: TrieNode()

        root = TrieNode()
        def insert(root, num):
            curr = root
            for i in reversed(range(32)):
                char = 1 if (num&(1<<i)) else 0
                if not curr.children[char]:
                    curr.children[char] = Trie()
                curr = curr.children[char]
            curr.is_end = True
        for num in nums:
            insert(root, num)
        def search(root, num):
            result = 0
            curr = root
            for i in reversed(range(32)):
                char = 1 if (num&(1<<i)) else 0
                if curr.children[1-char]:
                    result += (1<<i)
                    curr = curr.children[1-char]
                else:
                    curr = curr.children[char]
            return result

        maxx = 0
        for num in nums:
            maxx = max(maxx, search(root, num))
        return maxx

        