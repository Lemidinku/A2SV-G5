# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        st = ""
        count = 1
        for a in s:
            if a in st:
                count+=1
                st = a
            else: st+=a
        return count
            