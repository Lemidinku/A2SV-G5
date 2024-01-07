from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = defaultdict(int)
        max_len = float("-inf")
        l =0
        for r in range(len(s)):
            while table[s[r]]==1:
                table[s[l]]-=1
                l+=1
            table[s[r]]=1
            max_len = max(max_len, r-l+1)
        return max_len if max_len>float("-inf") else 0

        