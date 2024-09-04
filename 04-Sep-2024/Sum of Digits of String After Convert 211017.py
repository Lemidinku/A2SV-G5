# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        total =""
        for letter in s:
            val = ord(letter)-96
            total += str(val)

        for _ in range(k):
            temp = 0
            for a in total:
                temp += int(a)
            total = str(temp)
        return int(total)
        