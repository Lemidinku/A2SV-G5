# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        xor = 0
        for char in word:
            val = ord(char)-ord("a")
            xor ^= (1<<val)
            count += freq[xor]
            for i in range(10):
                num = xor^(1<<i)
                count += freq[num]
            freq[xor]+=1

        return count