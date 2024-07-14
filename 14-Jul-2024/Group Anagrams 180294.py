# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        table = defaultdict(list)
        for word in strs:
            letters = "".join(sorted([x for x in word]))
            table[letters].append(word)
        
        return [x for x in table.values()]